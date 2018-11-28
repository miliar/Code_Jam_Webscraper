#include<stdio.h>
#include<stdlib.h>
#define MAX(a,b) ((a > b) ? (a) : (b))
#define MIN(a,b) ((a < b) ? (a) : (b))

int main(){
	freopen("1A/A-large.in","r",stdin);
	freopen("1A/out.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int N;
		scanf("%d",&N);
		int * m = (int*)malloc(N*sizeof(int));

		int s=0,y=0,z=0;
		scanf("%d",&m[0]);
		for(int i=1;i<N;i++){
			scanf("%d",&m[i]);

			if(m[i-1] > m[i]){
				y += m[i-1]-m[i];
				s = MAX(s,m[i-1]-m[i]);
			}
		}
		for(int i=1;i<N;i++)z += MIN(m[i-1],s);

		printf("Case #%d: %d %d\n",t,y,z);
	}
}
