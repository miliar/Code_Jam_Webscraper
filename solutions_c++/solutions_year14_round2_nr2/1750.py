#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
	int tc=1,T;
	scanf(" %d",&T);
	for(tc=1;tc<=T;tc++){
		int A,B,K;
		scanf(" %d %d %d",&A,&B,&K);
		int ans=0,i,j;
		for(i=0;i<A;i++)
		for(j=0;j<B;j++)
			if((i&j) < K ) ans++;

		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
