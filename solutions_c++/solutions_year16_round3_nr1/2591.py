#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <unordered_map>
#include <ctime>
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

int main() {
	//freopen("A_small.in", "r", stdin);
	//freopen("A_small.out", "w", stdout);
	freopen("A_large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);
	ll T;
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		int pnum;
		cin >> pnum;
		char sp = 'A';
		priority_queue<pair<int, char>> pq;
		cout << "Case #" << t + 1 << ": ";
		for (int i = 0; i < pnum; i++) {
			int tmp;
			cin >> tmp;
			pq.push(make_pair(tmp, sp + i));
		}
		while (pq.size() > 2) {
			pair<int, char> top = pq.top(); pq.pop();
			cout << top.second << " ";
			top.first--;
			if (top.first > 0) pq.push(top);
		}
		pair<int, char> top = pq.top(); pq.pop();
		pair<int, char> second = pq.top(); pq.pop();
		for (int i = 0; i < top.first; i++) {
			cout << top.second << second.second << " ";
		}
		cout << endl;
	}
	return 0;
}