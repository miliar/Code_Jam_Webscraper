#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
char ch[210000];
int n,s[210000],head;
int solve(){
	scanf("%s",ch+1); n=strlen(ch+1);
	head=1; s[1]=1;
	for (int i=2;i<=n;i++)
		if (head==0||ch[s[head]]!=ch[i]) s[++head]=i; else head--;
	return n*5-head/2*5;
}
int main(){
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
