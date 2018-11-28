#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define rep(i,s,t) for(int i=int(s); i<int(t); i++)
#define mst(A,k) memset(A,k,sizeof(A))


int main() {
	freopen("D-small-attempt0.in","r",stdin); 
	freopen("ans.txt","w",stdout); 

	int Cas, k, c, s;
	scanf("%d", &Cas);
	rep(cas, 0, Cas)
	{
		scanf("%d%d%d", &k, &c, &s);
		ll d = 1;
		rep(i, 0, c - 1) d = d * k;
		printf("Case #%d: ", cas + 1);
		ll pos = 1;
		rep(i, 0, s)
		{
			if(i) printf(" ");
			printf("%lld", pos);
			pos += d;
		}
		printf("\n");
	}
	return 0;
}

