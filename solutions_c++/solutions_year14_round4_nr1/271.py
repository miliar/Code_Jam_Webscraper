#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("data.txt","w",stdout);
	int test; scanf("%d",&test);
	for(int T = 1; T <= test; ++T){
		printf("Case #%d: ",T);
		
		int n,m;
		scanf("%d%d",&n,&m);
		multiset<int> d;
		for(int i = 0; i < n; ++i){
			int k; scanf("%d",&k);
			d.insert(k);
		}
		
		int kq = 0;
		while (!d.empty()){
			kq++;
			int i = *d.begin(); d.erase(d.begin());
			auto p = d.upper_bound(m-i);
			if ( p == d.begin() ) continue;
			p--;
			if (i + *p <= m) d.erase(p);
		}
		printf("%d\n",kq);
	}

}