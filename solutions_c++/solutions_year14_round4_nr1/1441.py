#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>

#include <limits>
#include <algorithm>
#include <cmath>
#include <QString>
#include <QVector>
#include <QMap>
#include <QSet>

struct Solution
{
    void input(QTextStream &in)
    {
        in >> N >> X;
        S.resize(N);

        for (int i = 0; i < N; ++i)
            in >> S[i];
    }

    void solve()
    {
        ans = 0;

        std::sort(S.begin(), S.end());

        int i = 0, j = N - 1;
        while (i < j)
        {
            if ( S[i] + S[j] <= X )
            {
                ++ans;
                ++i;
                --j;
            }
            else
            {
                ++ans;
                --j;
            }
        }

        if (i == j)
            ++ans;
    }

    void output(QTextStream &out)
    {
        out << ans << "\n";
    }

public:
    // input:
    int N, X;
    QVector<int> S;

    // output:
    int ans;
};

#endif // SOLUTION_HPP
