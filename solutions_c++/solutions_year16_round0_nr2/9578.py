#include<bits/stdc++.h>
using namespace std;

int caso = 0;

void doit(){
	string s;
	cin>>s;
	s+="+";
	int sz = s.size();
	int ans = 0;
	for( int i=0 ; i<sz-1; ++i ){
		if( s[ i ] != s[ i+1 ] ) ans++;
	}
	printf("Case #%d: %d\n", ++caso, ans);
}

int main(){
	int tc;
	scanf("%d", &tc);
	while( tc-- )doit();
}
