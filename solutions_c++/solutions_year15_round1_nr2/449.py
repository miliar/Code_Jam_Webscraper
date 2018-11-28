#include <iostream>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

typedef long long LL;

struct Person {
	int id;
	LL next_time;
	Person(int _id, LL _n) {
		id = _id;
		next_time = _n;
	}
	bool operator<(const Person &p) const {
		if (next_time != p.next_time) {
			return next_time > p.next_time;
		}
		return id > p.id;
	}
};

int main() {
	freopen("C:/Users/dd/Downloads/B-large.in", "r", stdin);
	freopen("C:/Users/dd/Downloads/B-large.out", "w", stdout);

	int cas;
	cin >> cas;
	for (int te = 1; te <= cas; te ++) {
		vector<int> v;
		int B, N;
		cin >> B >> N;
		vector<int> vb;
		for (int i = 0; i < B; i ++) {
			int t; cin >> t;
			vb.push_back(t);
		} 
		if (N <= B) {
			printf("Case #%d: %d\n", te, N);
			continue;
		}
		LL lo = 0, hi = 1LL << 62, mid;
		while (true) {
			mid = (lo + hi) / 2;
			double sum = 0;
			for (int i = 0; i < B; i ++) {
				sum += mid / vb[i] + 1;
			}
			if (sum < N - 5*B) {
				lo = mid;
			} else if (sum < N) {
				break;
			} else {
				hi = mid;
			}
			//cout << mid << ' ' << sum << endl;
		}
	//	cout << mid << endl;
		LL now = 0;
		priority_queue<Person> pq;
		for (int i = 0; i < B; i ++) {
			now += mid / vb[i];
			now ++;
			pq.push(Person(i, (mid / vb[i] + 1) * vb[i]));
		}
		int id = 0;
		while (now < N) {
			now ++;
			Person p = pq.top();
			pq.pop();
			id = p.id;
			p.next_time += vb[id];
			pq.push(p);
			//printf("now = %lld, id = %d\n", now, id);
		}
		//cout << ma << endl;
		printf("Case #%d: %d\n", te, id + 1);
	}
}
