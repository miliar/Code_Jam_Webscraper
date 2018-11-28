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

set<int>myset;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("Aout-large.in", "w", stdout);
    int test;
    LL n, temp;
    scanf("%d", &test);
    for(int caseno = 1; caseno<=test; caseno++)
    {
        scanf("%lld", &n);
        myset.clear();
        bool flag = false;
        printf("Case #%d: ", caseno);
        for(int i=1; i<=100000; i++)
        {
            LL num = (i*n);
            temp = num;
            while(num)
            {
                myset.insert(num%10);
                num = num/10;
            }
            if(myset.size()==10)
            {
                printf("%lld\n", temp);
                flag = true;
                break;
            }
        }
        if(!flag) printf("INSOMNIA\n");
    }
    return 0;
}
