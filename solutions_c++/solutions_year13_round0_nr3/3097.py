#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<ctype.h>
#include<queue>
#include<bitset>
#include<deque>
#include<set>
#include<math.h>
#include<functional>
#include<stack>
#include<map>
#include<vector>
#include<iostream>
#include<sstream>
#include <time.h> 
using namespace std;
#define FIN freopen("AC.in","r",stdin)

int vis[1009];
int f[10];
int ok(int x){
	int len = 0;
	while(x){
		f[len++] = x%10;
		x/=10;
	}
	for(int i=0; i<len/2; i++)
		if( f[i] != f[len-1-i])
			return 0;
	return 1;
}
void init(){
	//memset(vis, 0, sizeof(vis));
	for(int i=1; i<=1000; i++){
		int x = sqrt(.0+i);
		if(x*x == i && ok(i) && ok(x))
			vis[i] = 1;
		else
			vis[i] = 0;
	}
}
int main(){
	//freopen("AC.in", "r", stdin);
	//freopen("AC.out","w", stdout);
	int cas,a,b;
	int ca=1;
	scanf("%d", &cas);
	init();
	while(cas--){
		scanf("%d%d", &a, &b);
		int ans = 0;
		for(int i=a; i<=b; i++)
			if(vis[i])
				ans++;
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}
