#include <bits/stdc++.h>
using namespace std;

#define si(n) scanf("%d", &n)
#define sl(n) scanf("%I64d", &n)
#define sd(n) scanf("%lf", &n)
#define pi(n) printf("%d", n)
#define pl(n) printf("%I64d", n)
#define pd(n) printf("%lf", n)
#define spc printf(" ")
#define ntr printf("\n")
#define c(n) cin>>n
#define o(n) cout<<n
#define lin(n) getline(cin, n)
#define lp(i, m, n) for(i = m; i < n; i++)
#define lll long long
#define ul unsigned long long
#define pf printf
#define gtl(n) getline(cin,n)
#define sf scanf
#define hello int main()
#define bye return 0
#define ef else if
#define el else
#define mii map<int, int>
#define msi map<string, int>
#define mss map<string, string>
#define mll map<long long, long long>
#define mis map<int, string>
#define memset xx

hello
{
    freopen("in.in","r",stdin);
    freopen("out.o","w",stdout);

	int t, a[11] = {0}, i, n, in2, now, tmp, x, f, j;
	si(t);
	lp(i, 1, t+1)
	{
	    si(n);
	    pf("Case #%d: ", i);
	    if(n == 0) pf("INSOMNIA\n");
	    el
	    {
	        lp(j, 0, 10) a[j] = 0;
	        in2 = 1;
	        while(1)
            {
                now = n * in2;
                //o("now is "); o(now); ntr;
                tmp = now;
                while(tmp)
                {
                    x = tmp - (tmp/10)*10;
                    //o("x is "); o (x); ntr;
                    a[x] = 1;
                    tmp/=10;
                }
                f = 1;
                lp(j, 0, 10) if(a[j] == 0) f = 0;
                if(f == 1){pi(now); ntr; break;}
                in2++;
            }
	    }
	}
	bye;
}
