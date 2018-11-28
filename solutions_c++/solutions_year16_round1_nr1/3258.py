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

char s[2000], t[2000];
int n, i, j, id, T;

void solve() {
 	cin >> s;
 	n = strlen(s);
 	id++;
 	if (n == 1) {
 		cout << "case #" << id << ": " << s[0] << endl;
 		return;
 	}
 	i = 100;
 	j = 100;
 	t[i] = s[0];
 	if (s[1] >= s[0]) {
 		t[--i] = s[1];
 	} else {
 		t[++j] = s[1];
 	}
 	for (int k = 2; k < n; ++k) {
 		if (s[k] >= t[i]) 
 			t[--i] = s[k];
 		else
 			t[++j] = s[k];
 	}
 	cout << "Case #" << id << ": ";
 	for (int k = i; k <= j; ++k)
 		cout << t[k];
 	cout << endl; 
}


int main() {
	#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> T;
	while (T--) {
		solve();
	}
	

	return 0;
}
                                

