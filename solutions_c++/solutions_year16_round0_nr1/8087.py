#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//

int main(){
	FASTER;

//	int N = 1000000;
//	printf("%d\n", N);
//	for (int i = 0; i < N; ++i) {
//		printf("%d\n",i);
//	}
//	return 0;

	int t;
	int Case=1;
	cin >> t;

	while(t--){
		int n ;
		cin >> n;
		printf("Case #%d: ",Case++);

		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}

		ll i = 1;
		int X[10];
		MEM(X, 0);
		ll x = i * n;
		while(1){
			x = i * n;

//			printf("x = %lld\n",x);
			while(x){
				X[x %10] =1;
				x/=10;
			}
			bool ok = true;
			for (int j = 0; j < 10; ++j) {
				if(X[j] != 1)ok = false;
			}

			if(ok)break;

			i++;
		}
		printf("%lld\n", i * n);
	}

	return 0;
}
