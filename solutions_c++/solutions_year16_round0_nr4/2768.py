#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI 3.14159265358979323846
typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<VI> matrix;
const ll MOD = 1000000007LL;

vector<ll> v1, v2;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++){
		ll k, c, s;
		scanf("%lld %lld %lld", &k, &c, &s);
		v1.clear();
		v2.clear();
		for(int i=0; i<k; i++){
			v1.pb(i+1);
		}
		for(int i=0; i<c-1; i++){
			for(int j=0; j<k; j++){
				v2.pb((v1[j] - 1) * k + j + 1);
			}
			v1.clear();
			for(int j=0; j<k; j++){
				v1.pb(v2[j]);
			}
			v2.clear();
		}
		printf("Case #%d: ", tc);
		for(int i=0; i<k; i++){
			printf("%lld ", v1[i]);
		}
		printf("\n");
	}	
	return 0;
}