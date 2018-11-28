#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
#include<stdlib.h>

using namespace std;

typedef long long int lnt;
typedef double dou;

int n,x;
int s[50140];
void sol(int uuu){
	scanf("%d %d",&n,&x);
	for(int i=0;i<n;i++)scanf("%d",s+i);
	sort(s,s+n);
	int ans=0;
	for(int i=0;i<n;i++){
		for(;i<n-1&&s[i]+s[n-1]>x;n--,ans++);
		n--;
		ans++;
	}
	printf("Case #%d: %d\n",uuu,ans);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("pa_l.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)sol(ti);
	return 0;
}

