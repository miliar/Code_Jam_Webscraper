//#include <fstream> 
#include <iostream> 
#include <string> 
#include <list> 
#include <stack>
#include <sstream> 
#include <vector> 
#include <algorithm> 
#include <iomanip> 
#include <cmath>
#include <cstdio>
#include <map>
#include <queue>
#include <deque>
#include <set>
using namespace std;
 
int n, ans;
long long a, b, aa, bb;

bool check (long long a) {
	long long p = 1;
	while (p < a) {
		p *= 10;
	}
	p /= 10;
	while (a > 9) {
		if (a / p != a % 10) {
			return false;
		}
		a = a % p;
		a = a / 10;
		p /= 100;
	}
	return true;
}

int main () {
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    //freopen("algo2.in", "r", stdin);freopen("algo2.out", "w", stdout);
	cin >> n;
	for (int k = 1; k <= n; k++) {
		cin >> a >> b;
		//cout << check(a) << '\n' << check(b) << '\n';
		aa = sqrt(a);
		if (aa * aa < a) {
			aa++;
		}
		bb = sqrt(b);
		for (int i = aa; i <= bb; i++) {
			if (check(i) && check(i * i)) {
				//cout << i << ' ' << i * i << '\n';
				ans++;
			}
		}
		cout << "Case #"<< k << ": "<< ans << '\n';
		ans = 0;
	}

    return 0;
}