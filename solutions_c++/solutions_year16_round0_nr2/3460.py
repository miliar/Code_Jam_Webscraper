
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

    bool cur_x, next_x;
    int f;
    QString res;
    foreach(QString str, in)
    {
        f = 0;
        cur_x = str.at(0) == '+';
        for(int i = 1; i < str.length(); i++)
        {
            next_x = str.at(i) == '+';
            if(next_x != cur_x)
            {
                f++;
                cur_x = next_x;
            }
        }
        if(!cur_x)
            f++;
        res.setNum(f);
        out.append(res);
    }

    // ------------------------------------------------------------------------

    int __i = 1;
    foreach(QString str, out)
    {
        out_stream << "Case #" << __i << ": " << str << endl;
        __i++;
    }
}
