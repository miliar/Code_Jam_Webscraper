#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>

using namespace std;

int T;
int N, M;
long minN;
long minSub;
vector< pair<int, pair<bool, int> > > events; //True = on, false = off
vector< pair<int, int> > stations; ///Cost, number

void run()
{
    int cur = 0;
    int stationIndex = 0;
    int lastStation = 0;

    while (cur < 2*M)
    {
        pair<int, pair<bool, int> > curPair = events[cur];
        ///Increment costs
        //cout << cur << endl;
        if (cur!= 0 && stations.size() != 0)
        {
            int dif = curPair.first - lastStation;
            for (int i = 0; i < stations.size(); i++)
            {
                stations[i].first += dif;
            }
        }
        lastStation = curPair.first;

        if (!((curPair.second).first)) ///Enter point
        {
            stations.push_back(make_pair(0, (curPair.second).second));

        }else
        {

            int num = (curPair.second).second;
            stationIndex = stations.size()-1;
            while (num > 0)
            {
                int maxxy = min(num, stations[stationIndex].second);
                long dN = stations[stationIndex].first;
               // cout << "HI" << cur << " " << dN << " " << num << endl;

                long dS = (dN-1)*(dN)*(0.5);
                //dN %= 1000002013;
                dS %= 1000002013;
                //dN = (dN*maxxy)%1000002013;
                dS = (dS*maxxy)%(1000002013);
                //minN += dN; minN %= 1000002013;
                minSub += dS; minSub %= 1000002013;
                num -= maxxy;
                stations[stationIndex].second -= maxxy;
                if (stations[stationIndex].second ==0)
                {
                   // cout << "hi" << endl;
                    stations.erase(stations.begin() + stationIndex);
                }

                stationIndex--;
            }
        }
        cur++;
    }
    //cout << minN << " " << minSub << endl;
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        events.clear();
        stations.clear();
        cin >> N >> M;
        long maxNs = 0;
        long sub = 0;
        minN = 0;
        minSub = 0;
        for (int i= 0; i < M; i++)
        {
            int o, e, p;
            cin >> o >> e >> p;
            pair<int, pair<bool, int> > x;
            pair<int, pair<bool, int> > s;
            pair<bool, int> enter;
            enter.first = false;
            enter.second = p;
            pair<bool, int> exit;
            exit.first = true;
            exit.second = p;
            x.first = e;
            x.second = exit;
            s.first = o;
            s.second = enter;
            events.push_back(x);
            events.push_back(s);

           //maxNs += (e-o)*p;

           long temp = (e-o-1)*(e-o)*(0.5);
           temp %= 1000002013;
           temp *= p;
            temp %= 1000002013;
           sub += temp;
           sub %= 1000002013;
           //maxNs %= 1000002013;
        }

        sort(events.begin(), events.end());
        //cout << maxNs << " " << sub << endl;
        run();
        cout << "Case #" << caseNum << ": " << (minSub - sub) << endl;



    }





    return 0;
}
