#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <complex> 
#include <ctime>
#include <cstring>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int t = 0; t < tests; ++t) {
    	cout << "Case #" << t + 1 << ": ";
   		int n;
 	   	cin >> n;
 	   	vector<int> a(n);
 	   	cin >> a[0] >> a[1] >> a[2];
 	   	vector<int> v(1 << n);
 	   	for (int i = 0; i < n; ++i) {
 	   		for (int j = (1 << i) - 1; j >= 0; --j) {
 	   			v[2 * j + 1] = (v[j] + 1) % 3;
 	   			v[2 * j] = v[j];
 	   		}
 	   	}

 	   	vector<int> p(3);
 	   	vector<int> q = {0, 1, 2};
 	   	for (int i = 0; i < 1 << n; ++i)
 	   		++p[v[i]];

 	   	bool cor = false;
 	   	for (int i = 0; i < 6; ++i) {
 	   		bool f = true;
 	   		for (int j = 0; j < 3; ++j)
 	   			if (p[j] != a[q[j]])
 	   				f = false;
 	   		if (f) {
 	   			vector<string> ans(1 << n);
 	   			for (int j = 0; j < 1 << n; ++j) {
 	   				if (q[v[j]] == 0)
 	   					ans[j] = "R";
 	   				if (q[v[j]] == 1)
 	   					ans[j] = "P";
 	   				if (q[v[j]] == 2)
 	   					ans[j] = "S";
 	   			}
 	   			for (int j = n - 1; j >= 0; --j) {
 	   				for (int k = 0; k < 1 << j; ++k) {
 	   					if (ans[2 * k] + ans[2 * k + 1] < ans[2 * k + 1] + ans[2 * k])
 	   						ans[k] = ans[2 * k] + ans[2 * k + 1];
 	   					else 
 	   						ans[k] = ans[2 * k + 1] + ans[2 * k];
 	   				}
 	   			}
 	   			cout << ans[0] << endl;
 	   			cor = true;
 	   			break;
 	   		}
 	   		next_permutation(all(q));
 	   	}

 	   	if (!cor) 
 	   		cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}