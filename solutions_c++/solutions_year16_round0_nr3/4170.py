#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<set>
#include<unordered_set>
#include<algorithm>
#include<stack>
using namespace std;

int n = 16, J = 50;
int tot = 400000000;
vector<bool> p(tot, 1);
unordered_set<int> primer;
vector<int> primer_v;

int solve(long long x) {
	long long s = (long long)sqrt(x);
	for(int i=0;i<primer_v.size();i++) {
		if (primer_v[i] > s) break;
		if (x % primer_v[i] == 0) return primer_v[i];
	}
	return 0;
}

bool judge(int x) {
	vector<int> ans(11, 0);
	for(int i=2;i<=10;i++) {
		long long tmp = x, k = 1;
		long long now = 0;
		while(tmp) {
			if (tmp & 1) now += k;
			k *= i;
			tmp >>= 1;
		}
		int t = solve(now);
		if (t == 0) return false;
		ans[i] = t;	
	}	
	
	stack<int> num;
	while(x) { num.push(x & 1); x >>= 1; }
	while(!num.empty()) { printf("%d", num.top());num.pop();}
	
	for(int i=2;i<=10;i++) {
		printf(" %d", ans[i]);
	}
	printf("\n");
	return true;
}

void work() {
	for(int i=2;i<tot;i++) {
		if (!p[i]) {
			continue;
		}		
		primer.insert(i);
		primer_v.push_back(i);
		int tmp = i + i;
		while (tmp < tot) {
			if (p[tmp]) {
				p[tmp] = false;
			}
			tmp += i;
		}
	}
//	cout << primer.size() << endl;
//	return;
	int cnt = 0;
	for(int i=(1 << (n-1)) + 1; i<tot; i+= 2) {
		if (judge(i)) {
			cnt++;
		}
		if (cnt == J) break;
	}
	
}

int main() {
//	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t = 1;
//	scanf("%d\n", &t);
	for(int i=0;i<t;i++) {		
		printf("Case #%d:\n", i+1);
		work();
	}

	return 0;
}

