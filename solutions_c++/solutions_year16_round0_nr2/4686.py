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
    freopen("in2.in","r",stdin);
    freopen("out2.o","w",stdout);

	int t, i, n, in2, now, tmp, x, f, j, l;
	char a[105];
	si(t);getchar();
	lp(i, 1, t+1)
	{
	    gets(a);
	    pf("Case #%d: ", i);
	    l = strlen(a);
	    x = 0;
	    lp(j, 0, l-1) if(a[j] == '+' && a[j+1] == '-') x++;
	    x*=2;
	    if(a[0] == '-') x++;
	    pi(x); ntr;
	}
	bye;
}

