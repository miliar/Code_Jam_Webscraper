/*
Prashant Gupta(GHOST_YO)
IIITA
*/
/*
start of libraries to be included in the program
*/
#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cstring>
#include <ctime>
#include <stack>
#include <sstream>
#include <fstream>
#include <limits.h>
/*
end of libraries to be included in the program
*/
using namespace std;
/*
start of MACRO definition
*/
#define For(i,a,b) for(i=a;i<=b;i++)
#define Ford(i,a,b) for(i=a;i>=b;i--)
#define Rep(i,c) for((i=c.begin());i!=c.end();i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sr(x) (int)x.size()
#define modul 1000000007
#define nmax 500100
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {For(i,a,b) cout << x[i] << ' '; cout << endl;}
#define fillchar(x,a,b,delta) For(_,a,b) x[_]=delta;
#define FILL(a) memset(a,0,sizeof(a));
#define sc(a) scanf("%d", &a)
#define scl(a) scanf("%lld", &a)
#define scc(a) scanf("%c", &a)
#define scs(a) scanf("%s", a)
#define Bit(s,i) ((s&(1<<i))>0)
#define Two(x) (1<<x)
#define pii pair<int,int>
#define ll long long
#define e 1e-6
#define PI acos(-1)
#define piii pair < pii ,int >
#define make(a,b,c) mp(mp(a,b),c)
#define gc getchar
#define pc putchar
/*
end of MACRO definition
*/

int mn, maxtop;

void rec(priority_queue <int> q, int time)
{
    if(time == maxtop) return;

    mn = min(mn, time+q.top());
    if (q.top() != 1) {
        int x = q.top();
        q.pop();
        for (int i = 1; i <= x/2; i++) {
            priority_queue <int> tmp;
            tmp = q;
            tmp.push(i);
            tmp.push(x-i);
            rec(tmp, time+1);
        }
    }
}

int main()
{
    int t, n, x, i, u = 0;
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("ot.txt", "w", stdout);
    cin >> t;
    while (t--) {
        cin >> n;
        mn = INT_MAX;
        priority_queue <int> q;
        for (i = 0; i < n; i++) {
            cin >> x;
            q.push(x);
        }
        maxtop = q.top();
        rec(q, 0);
        cout << "Case #" << ++u << ": ";
        cout << mn << endl;
    }
    return 0;
}
