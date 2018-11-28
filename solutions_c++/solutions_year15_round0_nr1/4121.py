#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt,s,ans;
char ch;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d: ",tt);
		scanf("%d ", &n);
		s=0;
		ans=0;
		for (i=0; i<=n; ++i){
			scanf("%c", &ch);
			ans+=max(0, i-s);
			s+=max(0, i-s);
			s+=ch-'0';
		}
		printf("%d\n", ans);
	}
	return 0;
}
