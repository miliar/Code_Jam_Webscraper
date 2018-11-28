#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>

#include <QVector>

struct Solution
{
    void input(QTextStream &in)
    {
        in >> C >> F >> X;
    }

    double neededTime(int factories)
    {
        double time = 0;
        double cps = 2.0; // cookies per second

        for (int i = 0; i < factories; ++i)
        {
            time += C / cps;
            cps  += F;
        }

        time += X / cps;

        return time;
    }

    void solve()
    {
        QVector<double> time_buf;
        time_buf.push_back( neededTime(0) );

        int factories = 0;
        for (;;)
        {
            ++factories;
            time_buf.push_back( neededTime(factories) );

            if ( time_buf[factories] > time_buf[factories - 1] )
            {
                answer = time_buf[factories - 1];
                break;
            }
        }
    }

    void output(QTextStream &out)
    {
        out << QString::number(answer, 'f', 7) << "\n";
    }

protected:
    // input:
    double C, F, X;

    // results:
    double answer;
};

#endif // SOLUTION_HPP
