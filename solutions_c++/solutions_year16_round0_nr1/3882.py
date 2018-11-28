//Author: net12k44
#include <bits/stdc++.h>
using namespace std;

void update(int cur, set<int>& s){
	if (cur == 0)
		s.insert(0);
	
	while (cur>0){
		s.insert(cur%10);
		cur /= 10;
	}
}

void solve(){
	int n;
	scanf("%d",&n);
	set<int> s;
	for(int i = 1, cur=n; i < 500; ++i, cur+=n){
		update(cur, s);
		if (s.size() == 10){
			printf("%d\n", cur);
			return;
		}
	}
	printf("INSOMNIA\n");
}

int main(){
	freopen("file.out","w",stdout);
	int test; scanf("%d",&test);	
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}