#include<bits/stdc++.h>
#define DIST(x1,x2, y1, y2) (((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
#define CLR(a) a.clear()
#define VCLR(a, n) for(int i=0; i<=n+3; i++) a[i].clear()
#define SIZE(a) a.size()
#define ERASE(a, b) memset(a, b, sizeof a)
#define PB(a, b) a.push_back(b)
#define PB2(a,i,b) a[i].push_back(b)
#define LL long long
#define DBG cout<<"I Am Here"<<endl
#define DBGA(a) cout<<a<<endl
#define DBGI(b,a) cout<<b<<' '<<a<<endl
#define DBGL(i,s,e,b) or(int i=s; i<=e; i++) cout<<b<<endl
#define INF 1e9
#define II(a) scanf("%I64d", &a)
#define PP(a) printf("%I64d", a)
#define si(a) scanf("%d", &a)
#define pii pair<LL,LL>
#define MAX 100007
#define logbase(a, b) ( log10(a)/log10(b) )

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("Bout-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int caseno=1; caseno<=test; caseno++)
    {
        string str;
        cin>>str;
        int sz = str.size();

        char ch = '+';

        int cnt = 0;
        for(int i = sz-1; i>=0; i--)
        {
            if(str[i]!=ch)
            {
                cnt++;
                ch = str[i];
            }
        }
        printf("Case #%d: %d\n", caseno, cnt);
    }
    return 0;
}
