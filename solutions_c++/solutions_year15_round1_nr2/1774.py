#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#define MAXB 1002
using namespace std;

int b, n;
int barbers[MAXB], cutting[MAXB];

int gcd(int a, int b) {
    for (;;) {
        if(a == 0) return b;
        b %= a;
        if(b == 0) return a;
        a %= b;
    }
}

int findlcm(int a, int b) {
    int temp = gcd(a, b);
    return temp ? (a / temp * b) : 0;
}

int findB() {
	int lcm = accumulate(barbers, barbers + b, 1, findlcm);

	vector<queue<int> > v;
	vector<int> res;

	for(int i = 0; i < b; i++) {
		queue<int> q;
		for(int j = barbers[i]; j <= lcm; j += barbers[i]) q.push(j);
		v.push_back(q);
	}
	
	int limit = 0;
	for(int i = 0; i < b; i++) {
		limit += lcm/barbers[i];
		res.push_back(i);
	}

	//cout << "Limit: " << limit << endl;

	for(int i = 0; i < limit; i++) {
		int minj = v[0].front() == lcm? -1 : 0;

		for(int j = 0; j < b; j++)
			if((minj == -1 || v[j].front() < v[minj].front()) && v[j].front() != lcm) minj = j;

		if(minj != -1) {
			res.push_back(minj);
			v[minj].pop();
		}
	}

	//for(int i = 0; i < res.size(); i++) cout << (res[i] + 1) << " "; cout << endl;

	return res[(n-1) % limit] + 1;
}

int main() {
	int tc;
	scanf("%d", &tc);

	for(int t = 1; t <= tc; t++) {
		scanf("%d %d", &b, &n);
		for(int i = 0; i < b; i++) scanf("%d", &barbers[i]);

		printf("Case #%d: %d\n", t, findB());
	}

	return 0;
}
