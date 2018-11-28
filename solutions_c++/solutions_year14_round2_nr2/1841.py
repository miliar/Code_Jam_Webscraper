#include<stdio.h>
#include<algorithm>
using namespace std;
int main ()
{
	int T,ans;
	int A,B,K;
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		printf("Case #%d: ",_);
		scanf("%d%d%d",&A,&B,&K);
		ans =0 ;
		for(int i=0;i<A;i++){
			for(int j=0;j<B;j++){
				if((i&j)<K)
					ans++;
			}
		}
		printf("%d\n",ans);
	}
}
