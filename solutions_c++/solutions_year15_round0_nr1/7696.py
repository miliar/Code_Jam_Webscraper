#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <unordered_map>
#include <list>
#include <set>
#include <random>
#include <stack>
using namespace std;

typedef long long ll;

stack <time_t> time_stack;
void startTimer() {
	time_stack.push(clock());
}
double stopTimer() {
	double time = clock() - time_stack.top();
	time_stack.pop();
	return time / double(CLOCKS_PER_SEC);
}


#define MAXN 2010
#define INF 2140000000




int main() {
	ios::sync_with_stdio(false);
#ifdef _HOME_
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
	//freopen(TASK ".in", "r", stdin);
	//freopen(TASK ".out", "w", stdout);
#endif

	
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int n;
		cin >> n;

		int ans = 0, cur = 0;
		for (int i = 0; i < n + 1; i++) {
			char c;
			cin >> c;
			if (cur < i) {
				ans += i - cur;
				cur = i;
			}
			cur += int(c - '0');
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}


#ifdef _HOME_
	system("pause");
#endif

	return 0;
}