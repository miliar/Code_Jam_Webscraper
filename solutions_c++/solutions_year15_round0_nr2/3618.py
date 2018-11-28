/*
 * B.InfiniteHouseofPancakes.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Yasser
 */

#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<queue>

using namespace std;

vector<int> v;
priority_queue<int, vector<int> > pq;
int solve() {
	int sol = 0, y, x;
	while (true) {

		sort(v.begin(), v.end());
		x = v[v.size() - 1];
		y = 0;
		if (v.size() > 1)
			y = v[v.size() - 2];
		if (x < 1 + max(y, x - (x / 2))) {
			break;
		}
		v.push_back(v[v.size() - 1] / 2);
		v[v.size() - 2] -= v[v.size() - 1];
		sol++;
	}
	sort(v.begin(), v.end());
	return sol + v[v.size() - 1];
}

void print() {
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << endl;
}
int mx = 0;
int solve2() {
	int sol = 0, x;
	int res = mx;
	while (true) {
		sort(v.begin(), v.end());
		print();
		x = v[v.size() - 1];
		res = min(res, x + sol);
		if (x == 1 || sol > mx) {
			break;
		}
		v.push_back(x / 2);
		v[v.size() - 2] -= x / 2;
		sol++;
	}
	return res;
}

int solve3() {

	queue<priority_queue<int, vector<int> > > q;
	q.push(pq);
	int res = 10000000;
	priority_queue<int, vector<int> > p;
	int ind = 0;
	while (!q.empty()) {
		int sz = q.size();
		for (int i = 0; i < sz; i++) {
			p = q.front();
			q.pop();
			int x = p.top();
			p.pop();
			res = min(res, x + ind);

			for(int j =1; j*2 <= x; j++){

				priority_queue<int, vector<int> > p2 = p;
				p2.push(j);
				p2.push(x - j);
				q.push(p2);
			}

		}
		ind++;
		if(ind > res)
			return res;
	}

	return res;
}

int solve4(){

	int res = 10000000;
	int x;
	for(int i=1;i<=mx;i++) {
		int mn = 0;
		for(int j=0;j<v.size();j++) {
			x = v[j] / i;
			if(v[j]%i == 0)x--;
			mn += x;
		}
		res = min(res, mn+i);
	}
	return res;
}

int main() {
	freopen("test.in", "rt", stdin);
	freopen("results.txt","wt",stdout);

	int T, D;

	scanf("%d", &T);
	for (int tt = 0; tt < T; tt++) {
		scanf("%d", &D);
		v.clear();
		pq = priority_queue<int, vector<int> >();
		v.resize(D);
		mx = 0;
		for (int i = 0; i < D; i++) {
			scanf("%d", &v[i]);
			mx = max(mx, v[i]);
			pq.push(v[i]);
		}

		printf("Case #%d: %d\n", tt + 1, solve4());
	}

	return 0;
}

