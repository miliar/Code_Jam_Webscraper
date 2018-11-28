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
    freopen("Bresult.out", "w", stdout);
    int t;
	string str, ttr;
	scanf("%d", &t);
	int cs = 0;
	while(t--)
	{
		cin>>str;
		int cnt = 0;
		printf("Case #%d: ", ++cs);
		int sz = str.size();
		for(int i=0;i<sz;i++)
		{
			if(str[i]=='+')  cnt++;
		}
		if(cnt==sz)
		{
			printf("0\n");
			continue;
		}
        cnt = 0;
        while(1)
        {
            cnt = cnt + 1;
            ttr.clear();

            int i;
            for(i=sz-1; i>=0; i--)
            {
                if(str[i]=='-')  break;
            }
            for(int j=0; j<sz; j++)
            {
                if(j>i)
                    ttr = ttr + str[j];
                else
                {
                    if(str[j]=='+') ttr = ttr +'-';
                    else ttr = ttr + '+';
                }
            }
            int tot = 0;
            int tsz = ttr.size();
            for(int j=0; j<tsz; j++)
            {
                if(ttr[j]=='+') tot++;
            }
            if(tsz==tot) break;
            str = ttr;
        }
        printf("%d\n", cnt);
	}
	return 0;
}
