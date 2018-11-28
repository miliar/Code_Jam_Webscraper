#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <map>
#include <stack>

#define fi first
#define se second
#define mp make_pair
#define ll long long
#define pii pair <int, int>
#define vi vector <int>
#define REP(a,b) for(int a = 0; a < b; ++a)
#define FORU(a,b,c) for(int a = b; a <= c; ++a)
#define FORD(a,b,c) for(int a = b; a >= c; --a)
#define MOD 1000000000
#define MODLL 1000007LL
#define INF 2123123123
#define pb push_back
using namespace std;

int n, X, ar[10005];
int bit[10005];

void update(int x)
{
	for (int i = x; i <= n; i += i&-i)
		++bit[i];
}

int query(int x)
{
	if (x == 0)
		return 0;
	
	int res = 0;
	
	for (int i = x; i; i -= i&-i)
		res += bit[i];
		
	return res;
}

int main() {
	int T;
	bool flag[10005];
	
	scanf("%d", &T);
	
	FORU(tc, 1, T) {
		scanf("%d %d", &n, &X);
		
		ar[0] = 0;
		FORU(i, 1, n)
			scanf("%d", &ar[i]);
		
		sort(ar, ar + n + 1);
		
		// printf("%d\n", X);
		// FORU(i, 1, n)
			// printf("%d ", ar[i]);
		// puts("");
		
		int ans = 0;
		
		memset(flag, false, sizeof(flag));
		memset(bit, 0, sizeof(bit));
		
		FORD(i, n, 1) {
			if (query(i) - query(i - 1))
				continue;
			
			++ans;
			
			if (i == 1)
				continue;
			
			// printf("%d\n", i);
			
			int pos = (lower_bound(ar, ar + n + 1, X - ar[i] + 1) - ar) - 1;
			
			pos = min(pos, i - 1);
			
			// printf("%d %d\n", i, pos);
			
			if (query(pos) == pos)
				update(i);
			else {
				int kiri = 1, kanan = pos, ans = kanan;
				
				while (kiri <= kanan) {
					int mid = (kiri + kanan) >> 1;
					
					if ((mid == kanan) && ((query(mid) - query(mid - 1)) == 0)) {
						ans = mid;
						break;
					}
					
					int tgh = query(mid);
					int tgh2 = query(mid - 1);
					int knn = query(kanan);
					
					if ((knn - tgh2) != (kanan - mid + 1)) {
						kiri = mid + 1;
						ans = mid;
					}
					else
						kanan = mid - 1;
				}
				
				update(i);
				update(ans);
			}
			
			// FORU(j, 1, n)
				// printf("%d ", bit[j]);
			// puts("");
			
			// FORU(j, 1, n)
				// printf("%d ", query(j));
			// puts("");
		}
		
		printf("Case #%d: %d\n", tc, ans);
	}
}
