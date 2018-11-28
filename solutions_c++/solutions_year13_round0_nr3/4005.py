#include <stdio.h>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

bool test(long long x) {
	if (x == 0) return false;
	long long tx = x,tmp = 0;
	while (tx) {
		tmp = tmp * 10 + tx % 10;
		tx = tx / 10;
	}
	return tmp == x;
}

int power[] = {1,10,100,1000,10000,100000,1000000,10000000};

vector<long long>lst;

void dfs(int l,long long x) {
	if (l > 6) {
		if (test(x) && test(x * x)) 
			lst.push_back(x*x);
		return;
	}
	for (int i = 0;i < 3;i++) {
		dfs(l+1,x+i*power[l]);
	}
}

int main() {
	dfs(0,0);
	lst.push_back(9);
	sort(lst.begin(),lst.end());
	int T;
	scanf("%d",&T);
	for (int cas = 1;cas <= T;cas++) {
		long long a,b;
		scanf("%lld%lld",&a,&b);
		int cnt = 0;
		for (int i = 0;i < lst.size() && lst[i] <= b;i++) {
			if (lst[i] >= a && lst[i] <= b)
				cnt++;
		}
		printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}
