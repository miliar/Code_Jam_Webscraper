#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int T,tt,ans;
int a[10000];
int max(int a,int b){
	return a<b?b:a;
}
int min(int a,int b){
	return a<b?a:b;
}
void dfs(int d,int n){
	if(d>=ans)
		return;
	bool flag=true;
	for(int i=0;i<n;i++)if(a[i]){		
			flag=false;
		break;
	}
	if(flag){
		ans=min(d,ans);
		return;
	}		
	int iMax=0;
	for(int i=0;i<n;i++){
		if(a[iMax]<a[i])
			iMax=i;
	}
	//1
	int b[100];
	for(int i=0;i<n;i++){		
		b[i]=a[i];
		if(a[i])
			a[i]--;
	}
	dfs(d+1,n);
	
	for(int i=0;i<n;i++){
		a[i]=b[i];		
	}	
	//2
	int y=(a[iMax]+1)/2;
	for(int i=y;i<a[iMax];i++){
		a[n]=i;
		a[iMax]-=a[n];
		dfs(d+1,n+1);
		a[iMax]=a[n]+a[iMax];
	}

}
int main(){	
	//freopen("t.txt","r",stdin);
	//freopen("B.out","w",stdout);
	tt=1;
	scanf("%d",&T);
	int n;
	while(T--){
		scanf("%d",&n);
		ans=0x3f3f3f3f;			
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);			
		}		
		dfs(0,n);
		printf("Case #%d: %d\n",tt++,ans);
	}
    return 0;
}