#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define rep(i,s,t) for(int i=int(s); i<int(t); i++)
#define mst(A,k) memset(A,k,sizeof(A))

vector<ll> S;

ll toBase(int n, int base)
{
	ll ret = 0, p = 1;
	while(n)
	{
		ret += (n % 2) * p;
		n >>= 1;
		p *= base;
	}
	return ret;
}
bool check(int n)
{
	S.clear();
	rep(base, 2, 11)
	{
		ll N = toBase(n, base);
		bool have = false;
		for(ll i = 2; i * i <= N; i++)
			if(N % i == 0)
			{
				S.push_back(i);
				have = true;
				break;
			}
		if(!have) return false;
	}
	return true;
}
int main() {
	freopen("C-small-attempt0.in","r",stdin); 
	freopen("ans.txt","w",stdout); 

	int Cas, n, J;
	scanf("%d", &Cas);
	rep(cas, 0, Cas)
	{
		scanf("%d%d", &n, &J);
		printf("Case #%d:\n", cas + 1);
		rep(i, (1 << (n - 1)), (1 << n))
		{
			i++;
			if(check(i))
			{
				int p = n;
				while(p--)
				{
					printf("%d", (i >> p) & 1);
				}
				for(int i = 0; i < S.size(); i++)
				{
					printf(" %d", S[i]);
				}
				printf("\n");
				J--;
				if(J == 0) break;
			}
		}
	}
	return 0;
}

