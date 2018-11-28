#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

struct A {
	double x, y, z, vx, vy, vz;
};

int n, s;
vector <A> arr;

double sq(double x) {
	return x * x;
}

double dist(int i, int j) {
	return sqrt(sq(arr[i].x - arr[j].x) + sq(arr[i].y - arr[j].y) + sq(arr[i].z - arr[j].z));
}

bool can(double m) {
	int n = arr.size();
	queue <int> q;
	vector <bool> r(n, false);
	r[0] = 1;
	q.push(0);
	while (!q.empty()) {
		int v = q.front();
		if (v == 1)
			return true;
		q.pop();
		for (int i = 0; i < n; i++) {
			if (r[i])
				continue;
			if (dist(v, i) <= m) {
				r[i] = true;
				q.push(i);
			}
		}
	}
	return false;
}

double dummy() {
	double l = 0, r = 1e9;
	for (int i = 0; i < 200; i++) {
		double m = (l + r) / 2;
		if (can(m))
			r = m;
		else
			l = m;
	}
	return l;
}
	
void solve(int t) {
	cin >> n >> s;
	arr.clear();
	arr.resize(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i].x >> arr[i].y >> arr[i].z >> arr[i].vx >> arr[i].vy >> arr[i].vz;
	double ans = dummy();
	printf("Case #%d: %.9lf\n", t, ans);
}

int main() {
	//freopen("A-large.in", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++)
		solve(t);
}