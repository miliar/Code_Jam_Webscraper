#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <set>
#include <map>


using namespace std;

int const MAXN = 10000;

int x,n;
multiset<int> s;

void solve() {
	scanf("%d %d", &n, &x);
	for (int i=0; i<n; i++) {
		int temp;
		scanf("%d", &temp);
		s.insert(temp);
	}
	
	int sol = 0;
	
	while (!s.empty()) {
		set<int>::iterator i = s.begin();
		int a = (*i);
		// printf("Estraggo %d\n", a);
		s.erase(i);
		sol++;
		
		int remaining_space = x-a;
		set<int>::iterator j = upper_bound(s.begin(), s.end(), x-a);
		
		if ( j == s.begin() ) continue;
		j--;
		int b = (*j);
		// printf("Lo matcho con %d\n", b);
		assert( b <= remaining_space );
		s.erase(j);
	}
	
	printf("%d\n", sol);
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
