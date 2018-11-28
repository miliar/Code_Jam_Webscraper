#include<stdio.h>
#include<stdlib.h>

int main(){
	freopen("0Q/B-small-attempt1.in","r",stdin);
	freopen("0Q/out.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int D;
		scanf("%d",&D);

		int *p = (int*)malloc(D*sizeof(int));
		for(int i=0;i<D;i++)scanf("%d",&p[i]);

		int min = 1000;
		for(int g=1;g<=500;g++){
			int time=g;
			for(int i=0;i<D;i++)time += (p[i]-1)/g;
			min = min < time ? min : time;
		}

		printf("Case #%d: %d\n",t,min);
		free(p);
	}
}
