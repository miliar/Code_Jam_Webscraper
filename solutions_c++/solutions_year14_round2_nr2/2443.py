#include<cstdio>
#include<cctype>
#include<cstring>
#include<cmath>
#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<bitset>
#include<map>
#include<queue>
#include<stack>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define pb push_back
#define mp make_pair
#define INF 1e9
#define EPS 1e-9

int main()
{
	int t, n, a, b;
	
	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf("%d %d %d", &a, &b, &n);
		
		ll cnt = 0;
		for(int i=0; i<n; ++i)
			for(int j=0; j<a; ++j)
				for(int k=0; k<b; ++k)
					if((j & k) == i)
						++cnt;
		
		cout << "Case #" << tc << ": " << cnt << endl;
	}

	return 0;
}
