#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<queue>
using namespace std;
int main(){
	int cas,t,sum;
	int num;
	int maxx,tmp;
	int i,j,minn;
	int a[1005];

	freopen("B-small-attempt3.in","r",stdin);

	freopen("B-small-attempt3.out","w",stdout);
	scanf("%d",&t);
	cas=0;
	minn=10005;

	while(t--){
		minn=10005;
		maxx=-1;

		scanf("%d",&num);
		for(i=0;i<num;i++){
			scanf("%d",&a[i]);
			if(a[i]>maxx)
				maxx=a[i];
			
		}
	
		for(i=1;i<=maxx;i++){
			sum=0;
			for(j=0;j<num;j++){
				if(a[j]%i)
					sum+=(a[j]/i);
				else
					sum+=(a[j]/i-1);
				
			}
			tmp=sum+i;
		//	printf("tmp:%d\n",tmp);
			if(tmp<minn)
				minn=tmp;
		}
		printf("Case #%d: %d\n",++cas,minn);
		
		
	}
	return 0;


}
