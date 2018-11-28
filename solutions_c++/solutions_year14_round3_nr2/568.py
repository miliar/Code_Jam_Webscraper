#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>
#include <QVector>
#include <QPair>
#include <QString>
#include <QMap>
#include <algorithm>


struct Solution
{
    void input(QTextStream &in)
    {
        in >> N;
        cars.resize(N);

        for (int i = 0; i < N; ++i)
            in >> cars[i];
    }

    quint64 fac(int n)
    {
        if ( n < 2 )
            return 1;

        return n * fac(n - 1);
    }

    void solve()
    {
        ans = 0;

        std::sort(cars.begin(), cars.end());

        quint64 mult = 1;
        int cur = 1;
        for (int i = 1; i < N; ++i)
            if ( cars[i] == cars[i - 1] )
            {
                ++cur;
            }
            else
            {
                mult *= fac(cur);
                cur   = 1;
            }

        do
        {
            QMap<QChar, bool> map;

            QChar prev = cars[0][0];
            map[prev] = true;

            for (int i = 0; i < N; ++i)
                for (int j = 0; j < cars[i].size(); ++j)
                {
                    if ( map.contains( cars[i][j] ) && map[ cars[i][j] ] )
                    {
                        if ( cars[i][j] != prev )
                            goto FAIL;
                    }
                    else
                    {
                        map[ cars[i][j] ] = true;
                        prev = cars[i][j];
                    }
                }

            ans += mult;

            FAIL:;
        }
        while ( std::next_permutation(cars.begin(), cars.end()) );
    }

    void output(QTextStream &out)
    {
        out << ans << "\n";
    }

protected:
    // input:
    int N;
    QVector<QString> cars;

    // output:
    quint64 ans;
};

#endif // SOLUTION_HPP
