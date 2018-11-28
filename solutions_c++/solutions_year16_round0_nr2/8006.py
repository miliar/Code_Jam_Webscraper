#include<iostream>
#include<cstdio>
#include<algorithm>
#define N 10000
#include<cstring>
using namespace std;
int n;
char s[N];
int main(){
	//freopen("2.in","r",stdin);
	//freopen("2.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int bz=1;bz<=T;bz++){
		scanf(" %s",&s);
		n=strlen(s);
		int ans=0,x=0;
		for (int i=n-1;i>=0;i--)
			ans+=(x^(s[i]=='-')),x^=(x^(s[i]=='-'));
		printf("Case #%d: %d\n",bz,ans);
	}
	return 0;
}
