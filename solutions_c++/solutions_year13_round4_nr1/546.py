#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

const int mod = 1000002013;

typedef long long ll;

int tests,m,N;
ll n,cost1,cost2;
int start[1010],finish[1010],p[1010],a[3010];
ll s[3010];

ll get(int m)
{
	return ((ll)n*2-m+1)*m/2 % mod;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		
		cin >> n >> m;
		N = 0;
		cost1 = 0;
		for (int i=1;i<=m;i++)
		{
			cin >> start[i] >> finish[i] >> p[i];
			a[++N] = start[i];
			a[++N] = finish[i];
			cost1 = (cost1 + get(finish[i]-start[i]) * p[i]) % mod;
		}
		sort(a+1,a+N+1);
		N = unique(a+1,a+N+1) - a - 1;
		
		s[0] = 0;
		for (int i=1;i<=m;i++)
		{
			for (int j=1;j<N;j++)
				if (start[i] <= a[j] && a[j+1] <= finish[i])
					s[j] = (s[j] + p[i]) % mod;
		}
		
		//printf("s:\n"); for (int i=1;i<=N;i++) printf("%d %d\n",a[i],s[i]);
		cost2 = 0;
		int flag = 1;
		while (flag)
		{
			flag = 0;
			int lef = 0, rig;
			while (lef<N)
			{
				while (lef<N && s[lef]==0) lef++;
				if (lef>=N) break;
				flag = 1;
				rig = lef;
				while (s[rig]>0) rig++;
				ll mins = mod;
				for (int i=lef;i<rig;i++)
					mins = min(mins, s[i]);
				for (int i=lef;i<rig;i++)
					s[i] -= mins;
				//printf("# %d %d %d\n", lef,rig,mins);
				cost2 = (cost2 + get(a[rig]-a[lef]) * mins % mod) % mod;
				lef = rig+1;
			}
			
		}
		//debug(cost1);
		//debug(cost2);
		cout << "Case #" << test << ": " << (cost1-cost2+mod) % mod << endl;
	}
	
	return 0;
}
