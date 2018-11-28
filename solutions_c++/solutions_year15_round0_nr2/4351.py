#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>
#include <set>
#include <vector>
#include <queue>

using namespace std;
priority_queue<int> men;
priority_queue<int> men1;
int work;
int a;

int main() {
	if(fopen("input.in","r")) {
		freopen("input.in","r",stdin);
		freopen("output.out","w",stdout);
	}
	int casenum; cin >> casenum;
	for(int i = 1; i <= casenum; i++) {
		int empty;
		cin >> empty;
		for(int j = 1; j <= empty; j++) {
			cin >> a;
			men.push(a);
			men1.push(a);
		}
		int seconds = 0;
		int curct = men.top();
		while(men.top() > 3) {
			seconds++;
			work = men.top(); men.pop();
			men.push(work/2); men.push(work - work/2);
			curct = min(curct, seconds + men.top());
		}
		curct = min(curct, seconds + men.top());
		seconds = 0;
		while(men1.top() > 3) {
			seconds++;
			work = men1.top(); men1.pop();
			men1.push(work-3); men1.push(3);
			curct = min(curct, seconds + men1.top());
		}
		curct = min(curct, seconds + men1.top());
		men = priority_queue<int> ();
		men1 = priority_queue<int> ();
	// 	curct = min(curct, seconds + men.top());
	// 	men = priority_queue <int> ();
	// 	seconds = 0;
	// 	sort(men1.begin(), men1.end());
	// 	while(men1[empty-1] > 2) {
	// 		seconds++;
	// 		if(men1[empty-1] % 2 == 1) {
	// 			for(int i = 0; i < empty; i++) {
	// 				men1[i]--;
	// 			}
	// 		}
	// 		else {
	// 			work = men1[empty-1]; 
	// 			men1[empty-1] = work/2;
	// 			cout << work << ' ';
	// 			men1.push_back(work - work/2);
	// 			empty++;
	// 		}
	// 		sort(men1.begin(), men1.end());
	// 		curct = min(curct, seconds + men1[empty-1]);
	// 	}
	// 	men1 = vector<int> ();
		cout << "Case #" << i << ": " << curct << '\n';
	}
	return 0;
}