#include <iostream>
#include <cstdio>
#include <algorithm>
#include <functional>
using namespace std;
int in[110][110],a[10010];
bool ch[110][110];
bool check(int n,int m) {
	for(int i(0);i!=n;++i)
		for(int j(0);j!=m;++j)
			if(!ch[i][j]) {
				bool R(false),C(false);
				for(int k(0);k!=n;++k)
					R|=ch[k][j];
				for(int k(0);k!=m;++k)
					C|=ch[i][k];
				if(C&&R) return false;
			}
	return true;
}
int main() {
	int n,m,_,ca(0); cin>>_;
st:
	while(_--) {
		cin>>n>>m;
		memset(ch,0,sizeof ch);
		for(int i(0);i!=n;++i)
			for(int j(0);j!=m;++j) {
				cin>>in[i][j];
				a[i*m+j] = in[i][j];
			}
		printf("Case #%d: ",++ca);
		sort(a,a+m*n,greater<int>());
		int l = unique(a,a+m*n)-a;
		for(int i(0);i!=l;++i) {
			for(int j(0);j!=n;++j)
				for(int k(0);k!=m;++k)
					if(a[i]==in[j][k])
						ch[j][k] = true;
			if(!check(n,m)) {
				puts("NO");
				goto st;
			}
		}
		puts("YES");
	}
	return 0;
}
