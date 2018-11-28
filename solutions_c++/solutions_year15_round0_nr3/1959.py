#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

#define LL long long 
using namespace std;
const int maxn = 10005;
const int mp[4][4] = 
{
	{1,2,3,4},
	{2,-1,4,-3},
	{3,-4,-1,2},
	{4,3,-2,-1}
};
int op(int x,int y){
	int flag = 1;
	if( x*y<0 ) flag = -1;
	x = max(x,-x); 	y = max(y,-y);
	return flag*mp[x-1][y-1];
}


int n;
int L;
LL x;
char s[maxn];
int b[maxn];

int main(){

	int t; scanf("%d",&t);
	for(int it=1;it<=t;it++){
		scanf("%d%lld",&L,&x);
		scanf("%s",s);
		for(int i=0;i<L;i++){
			if ( s[i]=='1' ) b[i] = 1;
			if ( s[i]=='i' ) b[i] = 2;
			if ( s[i]=='j' ) b[i] = 3;
			if ( s[i]=='k' ) b[i] = 4;
		}

		int k = 1;
		for(int i=0;i<L;i++)
			k = op(k,b[i]);
		LL xx = x%4; int kk = 1;		
		for(int i=0;i<(int)xx;i++)
			kk = op(kk,k);
		k = kk;

		int k1 = 1 , k2 = 1 , ans1 = -1, ans2 = -1;
		for(int j=0;j<4;j++)
		for(int i=0;i<L;i++){
			k1 = op(k1,b[i]);
			if ( k1==2&&ans1==-1 ) ans1 = j*L+i;
			k2 = op(b[L-i-1],k2);
			if ( k2==4&&ans2==-1 ) ans2 = j*L+i;
		}

		bool ans = false;
		if ( k==-1 && ans1!=-1&&ans2!=-1 ){
			ans1++; ans2++;
			if ( (LL)ans1+(LL)ans2<x*L )
				ans = true;
		}

		printf("Case #%d: %s\n" ,it, ans?"YES":"NO");
	}

	return 0;
}