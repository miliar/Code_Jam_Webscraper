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

typedef long long ll;

int tests;
ll N,P,n,p,a;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		cin >> N >> P;
		cout << "Case #" << test << ": ";
		//printf("Case #%d: ",test);
		if (P == 1LL<<N)
		{
			//printf("%d %d\n", (1LL<<N)-1, (1LL<<N)-1);
			cout << (1LL<<N)-1 << " " << (1LL<<N)-1 << endl;
			continue;
		}
		p = P;
		ll i = N;
		while (p>0)
		{
			i--;
			p -= 1LL<<i;
		}
		cout << ((1LL<<(N-i)) - 2) << " ";
		
		n = 1LL<<N;
		a = 1LL<<N;
		i = N;
		while (n>P)
		{
			i--;
			n -= 1LL<<i;
		}
		a -= 1LL << (N-i);
		cout << a << endl;
		
	}
	
	return 0;
}
