#include<iostream>
#include<cstdio>
#define rep(i,j,k) for(i=j;i<=k;i++)
using namespace std;

int T,o,i,v,n,ans1,ans2,a[2000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	rep(o,1,T){
		scanf("%d",&n);
		rep(i,1,n)	
			scanf("%d",&a[i]);
		ans1=ans2=0;
		v=0;
		rep(i,2,n){
			if(a[i]<a[i-1])
				ans1+=(a[i-1]-a[i]);
			if (a[i-1]-a[i]>v)
				v=a[i-1]-a[i];
		}
		rep(i,1,n-1){
			if (a[i]>v)
				ans2+=v;
			else
				ans2+=a[i];
		}
		printf("Case #%d: %d %d\n",o,ans1,ans2);
	}
	return 0;
} 
