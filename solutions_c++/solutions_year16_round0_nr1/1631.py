//---------------------------JUGNU: LET YOUR LIGHT SHINE---------------------------//
#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%d",&a)
#define sm(a,b) scanf("%d%d", &a, &b)
#define pr(a) printf("%d\n", a)
#define pm(a,b) printf("%d %d\n", a, b)
#define cn(a) cin >> a
#define ct(a) cout << a << endl
#define isset(x,i) ((x>>i)&1)
#define MAXN 1000005
#define MOD 1000000007LL
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);

#define trace1(x)       cerr << #x << " : " << x << endl;
#define trace2(x, y)    cerr << #x << " : " << x << " | " << #y << " : " << y << endl;
#define trace3(x, y, z) cerr << #x << " : " << x << " | " << #y << " : " << y << " | " << #z << " : " << z << endl;
#define cline printf("---------------------------\n");
using namespace std;
int mark[10];
void digits(int x)
{
	while(x > 0)
	{
		mark[x%10] = 1;
		x /= 10;
	}
	return;
}
int main()
{
	int i, j, t, n, m, k, l, r, mini,cnt, maxi, temp, flag, result;
	sc(t);
	fre(cnt, 1, t)
	{
		sc(n);
		if(n == 0) printf("Case #%d: INSOMNIA\n", cnt);
		else
		{
			fr(i, 0, 10) mark[i] = 0;
			temp = n;
			flag = 1;
			while(flag)
			{
				flag = 0;
				digits(temp);
				fr(j, 0, 10) if(mark[j] == 0) flag = 1;
				temp = temp + n;
			}
			printf("Case #%d: %d\n", cnt, temp - n);
		}
	}
return 0;
}
