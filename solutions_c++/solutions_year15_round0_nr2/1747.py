#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <set>
#include <utility>
#include <stack>

#define rep(i,n) for(int i = 0; i < (n); i++)

using namespace std;

void solve();
void runCase();

int check(vector<int> &p,int a,int b) {
	rep(i,p.size()) {
		if(p[i] > b) {
			a -= ((p[i] + b - 1) / b - 1);
			if(a<0) return 0;
		}
	}
	return 1;
}

int go(vector<int> &p,int m) {
	for(int i = 0; i < m; i++) {
		if(check(p,i,m-i)) {
			return 1;
		}
	}
	return 0;
}

void runCase()
{
	int d;
	scanf("%d",&d);
	vector<int> p(d);
	rep(i,d) scanf("%d",&p[i]);
	sort(p.begin(),p.end());
	reverse(p.begin(),p.end());
	int max_p = p[0];
	
	int l,r,m;
	l = 1; r = max_p;
	for(;;) {
		m = l + ((r-l) >> 1);
		if(go(p,m)) {
			r = m;
		} else {
			l = m+1;
		}
		if(l>=r) break;
	}
	printf("%d\n",r);
	return;
	
	for(int i = 1; i <= max_p; i++) {
		if(go(p,i)) {
			printf("%d\n",i);
			return;
		}
	}
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	solve();
	return 0;
}
