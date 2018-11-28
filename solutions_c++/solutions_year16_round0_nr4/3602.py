#include<iostream>
#include<cstdio>
#include<cstring>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
int main(){
	int cas;
	cin >> cas;
	rep(Cas, 1, cas){
		printf("Case #%d: ",Cas);
		int k, c, s;
		cin >> k >> c >> s;
		rep(i, 1, s) printf("%d%c", i, i == s ? '\n' : ' ');
	}
	return 0;
} 
