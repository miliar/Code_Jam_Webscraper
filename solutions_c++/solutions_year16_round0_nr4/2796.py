
// Using Qt 5 (http://qt.io)

#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QList>
#include <QStringList>
#include <QTextStream>
#include <QtMath>
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

    QStringList list;
    foreach(QString str, in)
    {
        list = str.split(" ");
        str = "";
        for(quint64 i = 0; i < list.at(0).toULongLong(); i++)
            str.append(QString::number(((qRound64(qPow(list.at(0).toULongLong(), list.at(1).toULongLong() - 1)) * i) + 1)) + " ");
        str.chop(1);
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
