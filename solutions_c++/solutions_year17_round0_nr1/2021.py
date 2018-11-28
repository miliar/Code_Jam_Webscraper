#include <bits/stdc++.h>
using namespace std;
int d[10000];
int n;
int k;
int calc(int i){
	if(i>n-k){
		for(int j=0;j<n;j++){
			if(d[j]==0){
				return 100000000;
			}
		}
		return 0;
	}
	if(d[i]==1)	return calc(i+1);
	for(int j=i;j<i+k;j++){
		if(d[j]==0)
			d[j] = 1;
		else
			d[j] = 0;
	}
	return 1+calc(i+1);
}
int main(){
	//freopen("input.in","r",stdin);
	//freopen("output.in","w",stdout);
	int t;
	int ls;
	scanf("%d",&t);
	char s[10000];
	for(int u=1;u<=t;u++){
		scanf("\n%s %d",s,&k);
		n = strlen(s);
		for(int i=0;i<n;i++){
			if(s[i]=='+'){
				d[i] = 1;
			}
			else{
				d[i] = 0;
			}
		}
		int ans = calc(0);
		if(ans>=100000000){
			printf("Case #%d: IMPOSSIBLE\n",u);
		}
		else{
			printf("Case #%d: %d\n",u,ans);
		}
	}
	return 0;
}