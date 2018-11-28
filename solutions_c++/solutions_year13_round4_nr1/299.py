#include <cassert>
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <limits>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <functional>
#include <bitset>
#include <numeric>
#include <utility>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iomanip>
#include <algorithm>

using namespace std;

const long long MOD = 1000002013LL;
inline long long get_cost(const long long N, long long a, long long b)
{
    if(a > b){swap(a,b);}
    const long long x = b-a;
    return x*N - ((x)*(x-1)/2);
}

long long solve_case(const long long N, vector<pair<pair<long long, long long>, long long > > &v)
{
    const int M = v.size();
    long long out = 0;
    vector<pair<long long, long long> > events;
    sort(v.begin(), v.end());
    map<long long, long long> ma;
    for(int i=0;i<M;++i)
    {
        //entries[v[i].first.first] += v[i].second;
        events.push_back(make_pair(v[i].first.first, -v[i].second));
        events.push_back(make_pair(v[i].first.second, v[i].second));
        long long x = get_cost(N, v[i].first.first, v[i].first.second) % MOD;
        out += (x * v[i].second) % MOD;
        out %= MOD;
    }
    sort(events.begin(), events.end());
    for(int t=0;t<events.size();++t)
    {
        if(events[t].second < 0)
        {
            long long q = events[t].first;
            long long w = -events[t].second;
            ma[q] += w;
        }
        else
        {
            long long at = events[t].first;
            long long need = events[t].second;
            while(need > 0)
            {
                pair<long long, long long> p = *ma.rbegin();
                long long x = p.first;
                long long y = p.second;
                long long used = min(y,need);
                long long z = get_cost(N, x, at);
                z %= MOD;
                z *= used;
                z %= MOD;
                out += MOD-z;
                out %= MOD;
                need -= used;
                y -= used;
                if(y == 0){ma.erase(x);}
                else{ma[x] = y;}
            }
        }
    }
    //assert(ma.empty());
    return out;
}

int main(int argc, char **argv)
{
    int CASES;
    cin >> CASES;
    for(int cn=1;cn<=CASES;++cn)
    {
        long long N,M;
        cin >> N >> M;
        vector<pair<pair<long long, long long>,long long > > v;
        vector<long long> nn;
        for(int i=0;i<M;++i)
        {
            long long a,b,c;
            cin >> a >> b >> c;
            v.push_back(make_pair(make_pair(a,b),c));
        }
        printf("Case #%d: %lld\n", cn, solve_case(N, v));
    }
    return 0;
}
