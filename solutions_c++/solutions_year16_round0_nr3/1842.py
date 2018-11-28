//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long int
int main(void){
    int t;
    scanf("%d",&t);
    int n,x;
    scanf("%d%d",&n,&x);
    printf("Case #%d:\n",1);
    int ans[100];
    int i,j;
    for(i=0;i<(1<<(n/2-2))&&i<x;i++){
		LL d=(1LL<<(n/2-1))+((LL)i<<1)+1;
		for(j=0;j<n/2;j++){
			if(d&(1<<j)) ans[j]=1;
			else ans[j]=0;
		}
		for(j=n/2-1;j>=0;j--) printf("%d",ans[j]);
		for(j=n/2-1;j>=0;j--) printf("%d",ans[j]);
		for(j=2;j<=10;j++){
			if(j%2) printf(" %d",2);
			else{
				LL ans=0,dd=d,x=1;
				while(dd){
					if(dd&1) ans+=x;
					x*=j;
					dd>>=1;
				}
				printf(" %lld",ans);
			}
		}
		printf("\n");
	}
    return 0;
}
