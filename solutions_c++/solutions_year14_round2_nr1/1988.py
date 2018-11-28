#include <iostream>
#include <cstdio>
#include <string>
#include <sstream> 
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <ctime>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define vi vector<int>
#define SZ(x) ((int)(x.size()))
#define fi first
#define se second
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define DBG cerr << "debug here" << endl;
#define DBGV(vari) cerr << #vari<< " = "<< (vari) <<endl;

typedef long long num;
typedef double fl;

int main()
{
    ios_base::sync_with_stdio(0);
    int tests;
    cin >> tests;
    for(int t = 1; t <= tests; ++t)
    {
        int n;
        cin >> n;
        string s[100];
        for(int i = 0; i < n; ++i)
        {
            cin >> s[i];
        }
        vector<pair<char, int> > va, vb;
        char prev = s[0][0];
        int cnt = 1;
        for(int i = 1; i < s[0].length(); ++i)
        {
            if(s[0][i] != prev)
            {
                va.pb(mp(prev, cnt));
                prev = s[0][i];
                cnt = 1;
            }
            else
            {
                cnt++;
            }
        }
        va.pb(mp(prev, cnt));

        prev = s[1][0];
        cnt = 1;
        for(int i = 1; i < s[1].length(); ++i)
        {
            if(s[1][i] != prev)
            {
                vb.pb(mp(prev, cnt));
                prev = s[1][i];
                cnt = 1;
            }
            else
            {
                cnt++;
            }
        }
        vb.pb(mp(prev, cnt));
        int res = 0;
        int fail = 0;
        if(va.size() != vb.size())
        {
            fail = 1;
        }
        else
        {
            for(int i = 0; i < va.size(); ++i)
            {
                char ca = va[i].fi;
                char cb = vb[i].fi;
                if(ca != cb)
                {
                    fail = 1;
                    break;
                }
                res += abs(va[i].se - vb[i].se);
            }
        }
        cout << "Case #" << t << ": ";
        if(fail)
        {
            cout << "Fegla Won";
        }
        else
        {
            cout << res;
        }
        cout << endl;
    }
    return 0;
}
