#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>
#include<string>
#include<cstring>

using namespace std;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	for (int done = 0; done < t; done++) {
		int n;
		cin >> n;
		priority_queue<pair<int,int>> p;
		for (int i = 0; i < n; i++) {
			int t;
			cin >> t;
			p.push(make_pair(t, i));
		}
		cout << "Case #" << done + 1 << ": ";
		while (p.size() != 0) {
			pair<int, int> first = p.top();
			p.pop();
			if (p.size() == 1) {
				pair<int, int> second = p.top();
				p.pop();
				if (second.first == first.first) {
					second.first -= 1;
					first.first -= 1;
					cout << (char)('A' + first.second) << (char)('A' + second.second) << ' ';
				}
				else {
					first.first -= 1;
					cout << (char)('A' + first.second) << ' ';
					/*if (first.first > 0) {
						p.push(first);
					}*/
				}
				if (second.first > 0) {
					p.push(second);
				}
				if (first.first > 0) {
					p.push(first);
				}
			}
			else {
				first.first -= 1;
				cout << (char)('A' + first.second) << ' ';
				if (first.first > 0) {
					p.push(first);
				}
			}
		}
		cout << endl;
	}
	return 0;
}