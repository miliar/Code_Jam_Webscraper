
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )

using namespace std;
typedef pair<int,int> PII;
typedef long long int LL;

LL n,p;

LL solve1(){
	LL x = 0;
	for(int i=(n-1); i>=0; i--){
		x = x+(1LL<<i);
		if(p<=x) return (1LL<<(n-i))-2;
	}
	return (1LL<<n)-1;
}


LL solve2(){
	if( p==1LL ) return 0;
	LL x;
	for(int i=2; i<=n; i++){
		x = (1LL<<i);
		if(p<x) return (1LL<<n)-(1LL<<(n+1-i));
	}
	return (1LL<<n)-1;
}

int main(){
	int zn;
	scanf("%d",&zn);
	for(int zi=1; zi<=zn; zi++){
		cin >> n >> p;
		LL a1=solve1();
		LL a2=solve2();

		printf("Case #%d: ",zi);
		cout << a1 << ' ' << a2 << endl;
	}
	return 0;
}

