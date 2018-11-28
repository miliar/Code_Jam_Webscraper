#include<cstdio>
int main() {
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		int A,B,K;
		scanf("%d%d%d",&A,&B,&K);
		int c=0;
		for(int i=0;i<A;i++)
			for(int j=0;j<B;j++)
				if((i&j)<K)
					c++;
		printf("Case #%d: %d\n",tc,c);
	}
	return 0;
}

