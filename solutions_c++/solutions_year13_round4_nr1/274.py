#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
const int magic = 1000002013;

int N;

int cost(int l,int p)
{
    long long c = ((N+N-l+1)*((long long)l))/2;
    c %= magic;
    c *= p;
    return c%magic;
}

int main()
{
    int T;
    cin >> T;
    for(int it=1;it<=T;it++)
    {
        int M;
        cin >> N >> M;
        long long cost1 = 0;
        long long cost2 = 0;
        vector<pair<int,int> > events;
        for(int i=0;i<M;i++)
        {
            int o,e,p;
            cin >> o >> e >> p;
            cost1 += cost(e-o,p);
            events.push_back(make_pair(o,-p));
            events.push_back(make_pair(e,p));
        }
        sort(events.begin(),events.end());
        vector<pair<int,int> > S;
        for(int i=0;i<events.size();i++)
        {
            int t = events[i].first;
            int p = events[i].second;
            if(p<0)
            {
                S.push_back(make_pair(t,-p));
            }
            else
            {
                while(p>0)
                {
                    int pp = min(p,S.back().second);
                    int tt = S.back().first;
                    cost2 += cost(t-tt,pp);
                    p -= pp;
                    S.back().second -= pp;
                    if(S.back().second == 0)
                        S.pop_back();
                }
            }
        }
        cost1 %= magic;
        cost2 %= magic;

        int ans = (cost1 + magic - cost2)%magic;


        cout << "Case #" << it << ": " << ans << endl;

    }
}
