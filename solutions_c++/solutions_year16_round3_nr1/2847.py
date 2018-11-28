#include<iostream>
#include<queue>
using namespace std;

struct node {
	int x;
	char ss;
	bool operator <(const node &a) const {
		return x < a.x;
	}
};

int jud1(priority_queue<node> q, int tot){
	node p = q.top();q.pop();
	if (p.x < 2) {
		return 0;
	}
	p.x -= 2;
	q.push(p);
	if (q.top().x * 2 > tot - 2) return 0;
	return 1;
}

int jud2(priority_queue<node> q, int tot){
	node p1 = q.top();q.pop();
	node p2 = q.top();q.pop();
	p1.x--;p2.x--;
	q.push(p1);q.push(p2);
	if (q.top().x * 2 > tot - 2) return 0;
	return 1;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("data.out", "w", stdout);
	int T, cas = 1;
	cin >> T;
	while (T--) {
		cout << "Case #" << cas++ << ":";
		int n, tot = 0;
		cin >> n;
		priority_queue<node> Q;
		Q.empty();
		node tmp;
		for (int i = 0; i < n; i++) {
			cin >> tmp.x;
			tot += tmp.x;
			tmp.ss = 'A' + i;
			Q.push(tmp);
		}
		if (tot % 2 == 1) {
			node a = Q.top();
			Q.pop();
			cout << " " << a.ss;
			a.x--;
			tot--;
			if (a.x > 0) {
				Q.push(a);
			}
		}
		while (!Q.empty()) {
			/*if (!Q.empty() && Q.top().x * 2 > tot) {
				cout << "fuck" << endl;
			}
			node a = Q.top();
			Q.pop();
			node b = Q.top();
			Q.pop();
			if (a.x * 2 > tot) {//
				a.x -= 2;
				tot-=2;
				cout << " " << a.ss << a.ss;
				if (a.x > 0) {
					Q.push(a);
				}
				Q.push(b);
				if (!Q.empty() && Q.top().x * 2 > tot) {
					cout << "fuck" << endl;
				}
			} else {
				a.x--;
				b.x--;
				tot-=2;
				cout << " " << a.ss << b.ss;
				if (a.x > 0) {
					Q.push(a);
				}
				if (b.x > 0) {
					Q.push(b);
				}
			}*/
			if (jud1(Q, tot)) {
				node a = Q.top();
				Q.pop();
				cout << " " << a.ss << a.ss;
				tot-=2;
				a.x-=2;
				if (a.x > 0) {
					Q.push(a);
				}
			} else if (jud2(Q, tot)) {
				node a = Q.top();
				Q.pop();
				node b = Q.top();
				Q.pop();
				a.x--;
				b.x--;
				cout << " " << a.ss << b.ss;
				tot-=2;
				if (a.x > 0) {
					Q.push(a);
				}
				if (b.x > 0) {
					Q.push(b);
				}
			} else {
				node a = Q.top();
				Q.pop();
				cout << " " << a.ss;
				tot--;
				a.x--;
				if (a.x > 0) {
					Q.push(a);
				}
			}
		}
		cout << endl;
	}
	return 0;
}
