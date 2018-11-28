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
    int tests;
    cin >> tests;
    for(int t = 1; t <= tests; ++t)
    {
        vector<int> cnt(16);
        int r[2];
        for(int k = 0; k < 2; ++k)
        {
            cin >> r[k];
            --r[k];
            for(int i = 0; i < 4; ++i)
            {
                for(int j = 0; j < 4; ++j)
                {
                    int v;
                    cin >> v;
                    if(i == r[k]) cnt[v - 1]++;
                }
            }
        }
        int n = 0;
        int ans;
        for(int i = 0; i < 16; ++i)
        {
            if(cnt[i] == 2)
            {
                ++n;
                ans = i + 1;
            }
        }
        cout << "Case #" << t << ": ";
        if(n == 1) cout << ans;
        else if(n == 0) cout << "Volunteer cheated!";
        else cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}
