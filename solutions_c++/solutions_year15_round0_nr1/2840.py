#include<iostream>
#include<cstdio>
#define FOR(i,l,r) for(int i = l; i <= r; i++)
using namespace std;

void deal(int T){
	int n,ans = 0,s = 0;
	cin >> n;
	getchar();
	FOR(i,0,n){
		if (s < i){
			ans += i - s;
			s = i;
		}
		s += getchar() - '0';
	}
	printf("Case #%d: %d\n",T,ans);
}

int main(){
	int T;
	cin >> T;
	FOR(i,1,T) deal(i);
	return 0;
}
