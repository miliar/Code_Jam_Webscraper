#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
#include<stdlib.h>

using namespace std;

typedef long long int lnt;
typedef double dou;

int f(int*a,int n){
	if(n==1){
		return 0;
	}
	int mn=1<<30,ll=n+1,rr=-1;
	for(int i=0;i<n;i++){
		if(mn>a[i]){
			mn=a[i];
			ll=rr=i;
		}
		else if(mn==a[i]){
			ll=min(ll,i);
			rr=max(rr,i);
		}
	}
	if(ll>n-1-rr){
		for(int i=rr;i+1<n;i++){
			swap(a[i],a[i+1]);
		}
		return f(a,n-1)+n-1-rr;
	}
	for(int i=ll;i-1>=0;i--){
		swap(a[i],a[i-1]);
	}
	return f(a+1,n-1)+ll;
}
int n;
int a[15140];
void sol(int uuu){
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",a+i);
	
	int ans=f(a,n);
	printf("Case #%d: %d\n",uuu,ans);
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("pb_l.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)sol(ti);
	return 0;
}

