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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++){
		int n;
		scanf("%d", &n);
		int mask = 0;
		int mul = 1;
		for(; mul <= 100; mul++){
			int cur = mul * n;
			while(cur){
				int x = cur % 10;
				mask |= (1 << x);
				cur /= 10;
			}
			if(mask == (1 << 10) - 1){
				break;
			}
		}
		if(mask == (1 << 10) - 1){
			printf("Case #%d: %d\n", tc, n * mul);
		}else{
			printf("Case #%d: INSOMNIA\n", tc);
		}

	}	
	return 0;
}