#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;

int DWar(list<double> naomis_logs, list<double> kens_logs)
{
    int naomi_score = naomis_logs.size();
    while(naomis_logs.size())
    {
        if(naomis_logs.back() < kens_logs.back())
        {
            naomi_score -= 1;
            naomis_logs.pop_front();
            kens_logs.pop_back();
        }
        else
        {
            naomis_logs.pop_back();
            kens_logs.pop_back();
        }
    }
    return naomi_score;
}

int War(list<double> naomis_logs, list<double> kens_logs)
{
    int naomi_score = naomis_logs.size();
    while(naomis_logs.size())
    {
        double chosen_naomi = naomis_logs.front();
        double chosen_ken;
        auto iter = kens_logs.begin();
        for ( auto i =  kens_logs.begin(); i != kens_logs.end(); ++i)
        {
            chosen_ken = *i;
            iter = i;
            if (chosen_ken > chosen_naomi)
            {
                naomi_score -= 1;
                break;
            }
        }
        kens_logs.erase(iter);
        naomis_logs.pop_front();
    }
    return naomi_score;
}

int main(int argc, char *argv[])
{
    freopen(argv[1], "r", stdin);
    freopen("output.txt", "w", stdout);

    int total_cases;
    scanf("%d", &total_cases);

    for (auto i = 0; i < total_cases; ++i)
    {
        int number_of_logs;
        scanf("%d", &number_of_logs);

        list<double> naomis_logs;
        list<double> kens_logs;

        for (auto j = 0; j < number_of_logs; ++j)
        {
            double t;
            scanf("%lf", &t);
            naomis_logs.push_back(t);
        }

        for (auto j = 0; j < number_of_logs; ++j)
        {
            double t;
            scanf("%lf", &t);
            kens_logs.push_back(t);
        } 

        naomis_logs.sort();
        kens_logs.sort();

        printf("Case #%d: %d %d\n", i+1, DWar(naomis_logs, kens_logs), War(naomis_logs, kens_logs));

    }
}
