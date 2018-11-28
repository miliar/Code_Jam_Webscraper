
// Using Qt 5 (http://qt.io)

#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QList>
#include <QStringList>
#include <QTextStream>
#include <QtMath>
#include "errno.h"

quint64 GetDiv(quint64 n, quint64 d)
{
    quint64 max = qFloor(qSqrt(n));
    for(quint64 i = d + 1; i < max; i++)
        if(n % i == 0)
            return i;
    return 0;
}

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

//    foreach(QString str, in)
//    {

//    }

    bool broke;
    quint64 c = 0x8001, n = 0, div[9], j, i;
    QString str;
    for(i = 0; i < 0xFFFF; i++)
    {
        broke = false;
        for(j = 2; j <= 10; j++)
        {
            div[j - 2] = GetDiv(QString::number(c, 2).toULongLong(nullptr, j), j);
            if(div[j - 2] == 0)
            {
                broke = true;
                break;
            }
        }
        if(!broke)
        {
            str.setNum(c, 2);
            for(j = 0; j < 9; j++)
                str.append(" " + QString::number(div[j]));
            out.append(str);
            n++;
            if(n == 50)
                break;
        }
        c += 2;
    }

    // ------------------------------------------------------------------------

    int __i = 1;
    out_stream << "Case #1: " << endl;
    foreach(QString str, out)
    {
        out_stream << str << endl;
        __i++;
    }
}
