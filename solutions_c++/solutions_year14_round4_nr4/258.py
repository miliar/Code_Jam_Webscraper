#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
#include<stdlib.h>

using namespace std;

typedef long long int lnt;
typedef double dou;

int m,n;
char *s[5140];
int sl[5140];
char sp[5140][200];
int cmp(char*a,char*b){
	int i=0;
	for(;a[i]&&a[i]==b[i];i++);
	return a[i]<b[i];
}
int lcp(char*a,char*b){
	int i=0;
	for(;a[i]&&a[i]==b[i];i++);
	return i;
}
int mylen(char*s){
	int i=0;
	for(;s[i];i++);
	return i;
}
int ins[5140];
int ans1;
int ans2;
char *ts[5140];
int tsl[5140];
int tst;
void dfs(int k){
	if(k==m){
		int tans=0;
		for(int i=0;i<n;i++){
			tst=0;
			for(int j=0;j<m;j++){
				if(ins[j]==i){
					ts[tst]=s[j];
					tsl[tst]=sl[j];
					tst++;
				}
			}
			if(tst==0){
				return;
			}
			tans+=tsl[0]+1;
			for(int j=1;j<tst;j++){
				tans+=tsl[j]-lcp(ts[j-1],ts[j]);
			}
		}
		if(tans>ans1){
			ans1=tans;
			ans2=1;
		}
		else if(tans==ans1){
			ans2++;
		}
		return;
	}
	for(int i=0;i<n;i++){
		ins[k]=i;
		dfs(k+1);
	}
}
void sol(int uuu){
	scanf("%d %d",&m,&n);
	for(int i=0;i<m;i++){
		scanf("%s",sp[i]);
		s[i]=sp[i];
	}
	sort(s,s+m,cmp);
	for(int i=0;i<m;i++){
		sl[i]=mylen(s[i]);
	}
	ans1=-1;
	ans2=0;
	dfs(0);
	printf("Case #%d: %d %d\n",uuu,ans1,ans2);
}

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("pd_s.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)sol(ti);
	return 0;
}

