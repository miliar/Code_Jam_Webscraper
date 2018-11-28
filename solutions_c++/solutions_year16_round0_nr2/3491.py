#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#define ll long long
#define f first
#define s second
#define mp make_pair
#define pb push_back

using namespace std;

int T, n, id;
char s[200];

bool ok() {
	for (int i = 0; i < n; ++i)
		if (s[i] == '-')
			return false;
	return true;
}

void rev() {
	for (int k = n - 1; k >= 0; --k) 
		if (s[k] == '-'){
			for (int i = 0, j = k; i < j; ++i, --j)
				swap(s[i], s[j]);
			for (int i = 0; i <= k; ++i)
				if (s[i] == '-')
					s[i] = '+';
				else
					s[i] = '-';
			return;
		}	
}

void print() {
	for (int i = 0; i < n; ++i)
		cout << s[i];
	cout << endl;
}

void solve() {	
	id++;
	scanf("%s", &s);
	n = strlen(s);
	ll ans = 0;
	while (!ok()) {
	        int cnt = 0, last = -1;
	        for (int i = 0; i < n; ++i) {
			if (s[i] == '+') {
				cnt++;
				last = i;
			} else
				break;						
	        }                     

	        if (cnt > 0) {
	        	ans++;
	        	for (int i = 0; i <= last; ++i)
	        		s[i] = '-';
	        }

		ans++;		
		rev();
	}
	printf("Case #%d: %d\n", id, ans);
}


int main() {
	#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	scanf("%d", &T);
	while (T--) {
		solve();
	}

	return 0;
}
                                

