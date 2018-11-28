#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ForC(i, n) for (int i = 0; i < int(n); i++)
#define ForD(i, n) for (int i = int(n-1); i >= 0; i--)

using namespace std;
const double PI = acos(-1.0);

typedef long long ll;
typedef pair<int, int> pii;

vector <int> v;
int n, j; 
bool flag;
ll base(ll base) {
	ll number = 1;
	ll aux = base;
	for (int i = v.size()-1; i>= 0; i--) {
		number += (v[i] * aux);
		aux *= base;
	}
	number += aux;
	ll k = sqrt(number);
	for (int i = 2; i <= k; i++) {
		if (number % i == 0) return i;		
	}
	flag = false;
	return -1;
}
int main (void) {
	int t;
	scanf("%d", &t);
	printf("Case #1:\n");
	scanf("%d %d", &n, &j);
	for (int i = 1; i < n-1; i++) v.pb(0);
	int counter = 0;
	while (true) {
		sort(v.begin(), v.end());
		do {
			flag = true;
			vector <ll> ans;
			for (int i = 2; i<= 10; i++) {
				ans.pb(base(i));
			}
			if (flag) {
				printf("1");
				for (int i = 0; i < v.size(); i++) printf("%d", v[i]);
				printf("1");
				for (int i = 0; i < ans.size(); i++) {
					printf(" %lld", ans[i]);
				}
				printf("\n");
				counter++;
			}
			if (counter == j) break;
		} while (next_permutation(v.begin(), v.end()));

		prev_permutation(v.begin(), v.end());
		v[v.size()-1] = 1;
		if (counter == j) break;
	}
	
	return 0;
}
