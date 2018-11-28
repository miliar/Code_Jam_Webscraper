#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

#define oo 1e9
#define pi 3.1415926536
#define all(x) x.begin(),x.end()
#define sorta(x) sort(all(x))
#define sortam(x,comp) sort(all(x),comp)
#define sortd(x) sort(x.rbegin(),x.rend())
#define pb push_back
#define mp make_pair
#define sf(x) scanf("%d", &x);
#define sfll(x) scanf("%I64d", &x);
#define pr(x) printf("%d ", x);

typedef long long ll;
using namespace std;
vector<int>a;

int go(int steps) {
	if(!steps) return oo;
	if(*max_element(all(a)) == 0) return 0;

	for(int i = 0; i < a.size(); i++) a[i]--;
	int ret = 1 + go(steps - 1);
	for(int i = 0; i < a.size(); i++) a[i]++;

	int ind = max_element(all(a)) - a.begin();
	
	for(int i = 1; i <= a[ind] / 2; i++) {
		a.push_back(i);
		a[ind] -= i;
		ret = min(ret, 1 + go(steps - 1));
		a[ind] += i;
		a.pop_back();
	}
	return ret;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	sf(t);
	for(int tc = 1; tc <= t; tc++) {
		int n;
		cin >> n;
		a.resize(n);
		for(int i = 0; i < n; scanf("%d", &a[i++]));
		sortd(a);
		int res = a[0], tmp = 0;
		/*
		while(a[0]>3) {
			res = min(res, tmp + a[0]);
			tmp++;
			a.push_back(a[0] / 2);
			a[0] -= a[0] / 2;
			sortd(a);
		}
		res = min(res, tmp + a[0]);*/
		printf("Case #%d: ", tc);
		cout << min(res,go(res)) << endl;
	}
	return 0;
}
