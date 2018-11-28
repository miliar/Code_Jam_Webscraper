#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <complex>
#include <time.h>

#define M_PI           3.14159265358979323846

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "1"

#pragma comment(linker, "/STACK:56777216")

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef pair<int, int> pii;

int main() {
	freopen(PROBLEM_ID".in", "r", stdin);
	freopen(PROBLEM_ID".out1", "w", stdout);
	
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		ll n;
		cin >> n;
		 cout << n << " ";
	
		ll answer = -1;
		set<int> seen;
		ll sum = 0;
		for (int j = 0; j < 1000000; ++j) {
			sum += n;
			cout << sum << " ";
			ll sumCopy = sum;
			while (sumCopy != 0) {
				seen.insert(sumCopy % 10);
				sumCopy /= 10;
			}
			if (seen.size() == 10) {
				answer = sum;
				break;
			}
		}
		cout << "Case #" << i + 1 << ": ";

		if (answer == -1) {
			cout << "INSOMNIA";
		}
		else {
			cout << answer;
		}
		cout << endl;
	}

	return 0;
}