
// Using Qt 5 (http://qt.io)

#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QList>
#include <QStringList>
#include <QTextStream>
#include <QChar>
#include "errno.h"

#define LOOP(start, end) for(int start = 0; start < (end); start++)
#define LOOP1(start, end) for(int start = 1; start <= (end); start++)

QFile in_file;
int NextInt(int base = 10);
QString NextString(QString delim = " \n");
QString s;
int Take(QString num_str, QChar ch)
{
    int cnt;
    int rem[20];

    for(int i = 0; i < s.length(); i++)
    {
        if(s.at(i) == ch)
            cnt++;
    }

    memset(rem, cnt, 20);
    for(int k = 0; k < cnt; k++)
    {
        for(int j = 0; j < num_str.length(); j++)
        {
            for(int i = 0; i < s.length(); i++)
            {
                if(num_str.at(j) == s.at(i))
                {
                    s.remove(i, 1);
                    break;
                }
            }
        }
    }

    return cnt;
}

int main(int argc, char **argv)
{
    if(argc < 2)
        return -EINVAL;

    QStringList out;
    QTextStream out_stream(stdout);
    int T;

    in_file.setFileName(argv[1]);
    if(!in_file.open(QIODevice::ReadOnly | QIODevice::Text))
        return -ENOENT;

    T = NextInt();

    // ------------------------------------------------------------------------

    int cnt[10];
    LOOP1(case_nr, T)
    {
        s = NextString();

        cnt[0] = Take("ZERO", 'Z');
        cnt[2] = Take("TWO", 'W');
        cnt[4] = Take("FOUR", 'U');
        cnt[6] = Take("SIX", 'X');
        cnt[1] = Take("ONE", 'O');
        cnt[3] = Take("THREE", 'R');
        cnt[7] = Take("SEVEN", 'S');
        cnt[5] = Take("FIVE", 'V');
        cnt[8] = Take("EIGHT", 'H');
        cnt[9] = Take("NINE", 'I');

        QString tmp = "";
        for(int i = 0; i < 10; i++)
        {
            for(int j = 0; j < cnt[i]; j++)
            {
                tmp.append(QString::number(i));
            }
        }
        out.append(tmp);
    }

    // ------------------------------------------------------------------------

    int __i = 1;
    foreach(QString str, out)
    {
        out_stream << "Case #" << __i << ": " << str << endl;
        __i++;
    }
}

int NextInt(int base)
{
    return NextString(" \n").toInt(nullptr, base);
}

qreal NextFloat(void)
{
    return NextString(" \n").toDouble();
}

QString NextString(QString delim)
{
    char c = '\0';
    QString s;

    do
    {
        in_file.read(&c, 1);
        s.append(c);
    } while(!delim.contains(c) && !in_file.atEnd());

    s.chop(1);

    return s;
}
