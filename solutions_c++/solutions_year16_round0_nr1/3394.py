
// Using Qt 5 (http://qt.io)

#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QList>
#include <QStringList>
#include <QTextStream>
#include "errno.h"

int main(int argc, char **argv)
{
    if(argc < 2)
        return -EINVAL;

    QFile in_file(argv[1]);
    QStringList in, out;
    QTextStream out_stream(stdout);

    if(!in_file.open(QIODevice::ReadOnly | QIODevice::Text))
        return -ENOENT;

    while(!in_file.atEnd())
    {
        QString str(in_file.readLine());
        if(str.right(1) == "\n")
            str.chop(1);
        in.append(str);
    }
    in_file.close();
    in.removeFirst(); // Number of cases

    // ------------------------------------------------------------------------

    quint32 n, x;
    quint16 r;
    QString res;
    foreach(QString str, in)
    {
        if(str.toInt() == 0)
        {
            out.append("INSOMNIA");
            continue;
        }

        r = 0;
        x = 1;
        n = str.toInt();
        while(r != 0x03FF)
        {
            str.setNum(n * x);
            x++;
            for(int i = 0; i < str.length(); i++)
                r |= 1 << str.at(i).digitValue();
        }
        out.append(str);
    }

    // ------------------------------------------------------------------------

    int __i = 1;
    foreach(QString str, out)
    {
        out_stream << "Case #" << __i << ": " << str << endl;
        __i++;
    }
}
