#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <cstring>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
using namespace std;

typedef long long ll;

ll heights[2510];

int main() {

	ll t, n;
	cin >> t;
	for(ll i = 0; i < t; i++) {
		cin >> n;
		memset(heights, 0, sizeof heights);
		ll aux;
		for(ll j = 0; j < (2 * n - 1) * n; j++) {
			cin >> aux;
			heights[aux]++;
		}
		bool first = true;
		cout << "Case #" << i + 1 << ": ";
		for(ll j = 0; j < 2510; j++) {
			if(heights[j] % 2 != 0) {
				if(!first)
					cout << " ";
				first = false;
				cout << j;
			}
		}
		cout << endl;
	}

	return 0;
}
