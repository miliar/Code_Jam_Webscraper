#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        vector<double> agg_buildfarmtime;
        vector<double> totaltimeary;
        double C, F, X;
        cin >> C >> F >> X;
        for(int j = 0; ; ++j) {
            double rate = 2.0 + F * j;
            if (j > 0) agg_buildfarmtime.push_back(agg_buildfarmtime[j-1] + C / rate);
            else agg_buildfarmtime.push_back(C / rate);
            double totaltime = j > 0 ? agg_buildfarmtime[j-1] : 0.0;
            totaltime += (X / rate);
            totaltimeary.push_back(totaltime);
            if (j > 0 && totaltimeary[j-1] <= totaltimeary[j])
                break;
        }
        printf("%.7f\n", totaltimeary[totaltimeary.size() - 2]);
    }
    return 0;
}
