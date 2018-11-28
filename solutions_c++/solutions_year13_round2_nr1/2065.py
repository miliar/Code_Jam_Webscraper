#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;
int n, ar[20],a,memo[3000][110];

int dp(int acum, int ind){
	if(ind>=n) return 0;

	int &ref = memo[acum][ind];

	if(ref!=-1) return ref;
	ref = 10000000;
	if(ar[ind]<acum) ref = dp(acum+ar[ind],ind+1);
	else{
		ref = min(ref,1+dp(acum+acum-1,ind));
		ref = min(ref,1+dp(acum,ind+1));
	}

	return ref;


}

int main(){

	int T;
	scanf("%d",&T);
	
	for(int p=0;p<T;p++){
		printf("Case #%d: ",p+1);
		memset(memo,-1,sizeof(memo));
		scanf("%d %d",&a, &n);	
		for(int x=0;x<n;x++) scanf("%d",&ar[x]);
		sort(ar,ar+n);

		printf("%d\n",dp(a,0));
	}

	return 0;
}
