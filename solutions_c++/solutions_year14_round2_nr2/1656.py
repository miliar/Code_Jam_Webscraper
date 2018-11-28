#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

int main() {
	int A,B,K,T;
	freopen("1.in","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&T);
	for(int tc=1;tc<=T;tc++) {
		scanf("%d%d%d",&A,&B,&K);
		int ans=0;
		int i,j;
		for(i=0;i<A;i++)
			for(j=0;j<B;j++) if((i&j)<K) ans++;
		printf("Case #%d: %d\n",tc,ans);
	}
}	
