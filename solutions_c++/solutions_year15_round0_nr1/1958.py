#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

using namespace std;
const int maxn = 1005;

int n;
char s[maxn];

int main(){

	int t; scanf("%d",&t);
	for(int it=1;it<=t;it++){
		scanf("%d%s",&n,s);
		int ans = 0 , sum = s[0]-'0';
		for(int i=1;i<=n;i++){
			int k = s[i]-'0';
			if ( k==0 ) continue;
			if( sum<i ){
				ans += i-sum;
				sum += i-sum;
			}
			sum += k;
		}
		printf("Case #%d: %d\n" ,it, ans);
	}

	return 0;
}