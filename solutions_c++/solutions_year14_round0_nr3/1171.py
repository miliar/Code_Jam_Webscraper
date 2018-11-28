#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>

#include <string>
#include <vector>
#include <QVector>

struct Solution
{
    typedef std::vector<std::string> Field;

    void input(QTextStream &in)
    {
        in >> R >> C >> M;

        field.resize(R);
        std::string filler(C, '*');
        for (int i = 0; i < R; ++i)
            field[i] = filler;

        M = R * C - M;
    }

    bool isValid(int r, int c) const
    {
        return !(r < 0 || c < 0 || r >= R || c >= C);
    }

    void dfs(int r, int c, int m, Field f)
    {
        if (m == M) throw f;

        int routes = 0;
        for (int dr = -1; dr <= 1; ++dr)
            for (int dc = -1; dc <= 1; ++dc)
                if ( isValid(r + dr, c + dc) && f[r + dr][c + dc] == '*' )
                {
                    f[r + dr][c + dc] = '.';
                    ++routes;
                }

        if ( routes == 0 || m + routes > M )
            return;

        for (int dr = -1; dr <= 1; ++dr)
            for (int dc = -1; dc <= 1; ++dc)
                if ( isValid(r + dr, c + dc) && (dr != 0 || dc != 0) )
                    dfs(r + dr, c + dc, m + routes, f);
    }

    void solve()
    {
        field[0][0] = '.';

        try
        {
            dfs(0, 0, 1, field);
        }
        catch (Field f)
        {
            impossible = false;
            field = f;

            return;
        }

        impossible = true;
    }

    void output(QTextStream &out)
    {
        if ( impossible )
        {
            out << "Impossible\n";
        }
        else
        {
            field[0][0] = 'c';

            for (int i = 0; i < R; ++i)
                out << field[i].c_str() << "\n";
        }
    }

protected:
    // input:
    int R, C, M;
    Field field;

    // results:
    bool impossible;
};

#endif // SOLUTION_HPP
