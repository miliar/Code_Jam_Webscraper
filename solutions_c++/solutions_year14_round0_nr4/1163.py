#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>

#include <QVector>
#include <algorithm>

struct Solution
{
    void input(QTextStream &in)
    {
        in >> N;

        double tmp;
        for (int i = 0; i < N; ++i)  { in >> tmp; naomi.push_back(tmp); }
        for (int i = 0; i < N; ++i)  { in >> tmp;   ken.push_back(tmp); }
    }

    bool naomiIsReadyToStrike() const
    {
        for (int i = 0; i < naomi.size(); ++i)
            if ( naomi[i] < ken[i] )
                return false;

        return true;
    }

    void solve()
    {
        deceitful_score = fair_score = 0;
        std::sort(naomi.begin(), naomi.end());
        std::sort(ken.begin(), ken.end());

        // fair and quare play
        QVector<double> ken_copy = ken;
        for (int i = N - 1; i >= 0; --i)
        {
            double chosen_naomi = naomi[i];

            QVector<double>::iterator it;
            it = std::upper_bound(ken_copy.begin(), ken_copy.end(), chosen_naomi);

            if ( it == ken_copy.end() )
            {
                // Ken can't beat our block
                ken_copy.removeAt(0);
                ++fair_score;
            }
            else
            {
                ken_copy.erase(it);
            }
        }

        // deceitful play
        while ( !naomiIsReadyToStrike() )
        {
            naomi.removeAt(0);
            ken.removeAt(ken.size() - 1);
        }

        deceitful_score = naomi.size();
    }

    void output(QTextStream &out)
    {
        out << deceitful_score << " " << fair_score << "\n";
    }

protected:
    // input:
    int N;
    QVector<double> naomi, ken;

    // results:
    int deceitful_score;
    int fair_score;
};

#endif // SOLUTION_HPP
