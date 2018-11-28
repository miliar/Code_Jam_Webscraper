#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>

#include <limits>
#include <algorithm>
#include <QString>
#include <QVector>
#include <QMap>
#include <QSet>
#include <cmath>

struct Solution
{
    void input(QTextStream &in)
    {
        QString s = in.readLine();
        s.replace('/', ' ');

        QTextStream ss(&s);
        ss >> A >> B;

    }

    quint64 gcd(quint64 a, quint64 b)
    {
        quint64 temp;
        while (b != 0)
        {
            temp = b;
            b    = a % b;
            a    = temp;
        }
        return a;
    }

    void minimize(quint64 &a, quint64 &b)
    {
        quint64 g = gcd(a, b);

        a /= g;
        b /= g;
    }

    void solve()
    {
        ans = 0;
        minimize(A, B);

        {
            quint64 k = 1;

            while ( k < B )
                k = (k << 1);

            if ( k != B )
            {
                ans = -1;
                return;
            }
        }

        while ( A < B )
        {
            ++ans;

            A = (A << 1);
            minimize(A, B);
        }
    }

    void output(QTextStream &out)
    {
        if ( ans < 0 )
        {
            out << "impossible\n";
        }
        else
        {
            out << ans << "\n";
        }
    }

public:
    // input:
    quint64 A, B;


    // output:
    qint64 ans;
};

#endif // SOLUTION_HPP
