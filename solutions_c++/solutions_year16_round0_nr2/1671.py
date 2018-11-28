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
#define MAXN 105
#define MOD 1000000007LL
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);

#define trace1(x)       cerr << #x << " : " << x << endl;
#define trace2(x, y)    cerr << #x << " : " << x << " | " << #y << " : " << y << endl;
#define trace3(x, y, z) cerr << #x << " : " << x << " | " << #y << " : " << y << " | " << #z << " : " << z << endl;
#define cline printf("---------------------------\n");
using namespace std;
char S[MAXN];
int main()
{
	int i, j, t, n, m, k, l, r, mini,cnt, maxi, temp, flag, result;
	char c, prev;
	sc(t);
	fre(cnt, 1, t)
	{
		result = 0;
		scanf("%s", S);
		temp = strlen(S);
		l = temp;
		frr(i, temp-1, 0)
		{
			if(S[i] == '+') l = i;
			else break;
		}
		if(l == 0) result = -1;
		else
		{
			prev = S[0];
			fr(i, 1, l)
			{
				if(S[i] != prev)
				{
					result++;	
					prev = S[i];
				} 
			}
		}
		printf("Case #%d: %d\n", cnt, result + 1);
	}
return 0;
}
