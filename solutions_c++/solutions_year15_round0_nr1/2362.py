#include<bits/stdc++.h>
 
using namespace std;

#define N	5010

char s[N];

int main(){
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i<=T ; i++ ){
		int Smax;
		scanf("%d",&Smax);
		scanf("%s",s);
		int c = s[0] - '0';
		int ans = 0;
		for( int j = 1 ; j <= Smax ; j++ ){
			int demand = j;
			if( demand > c && s[j] > '0'){
				ans += demand - c;
				c = demand + s[j] - '0';
			}
			else{
				c += ( s[j] - '0' );
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}       
