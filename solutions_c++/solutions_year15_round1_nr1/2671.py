#include<stdio.h>
FILE *out = fopen("output.txt", "w");
int m[10000];
int max;
int T;
int N;
int res1,res2;
int pre;

void init(){
	int i;
	max = 0;
	for(i=0;i<1005;i++)
		m[i] = 0;
	res1 = 0;
	res2 = 0;
	N = 0;
	pre = 0;
}
void main(){
	scanf("%d",&T);
	int i;
	int j;
	for(i=0;i<T;i++){
		init();
		scanf("%d",&N);
		for(j=0;j<N;j++){
			scanf("%d",&m[j]);
			if(j>0){
				if(m[j]<m[j-1]){
					res1 += m[j-1]-m[j];
					if(max<m[j-1]-m[j])
						max = m[j-1]-m[j];
				}
			}
		}
		for(j=0;j<N-1;j++){
			if(m[j]>max)
				res2 += max;
			else
				res2 += m[j];
		}
		fprintf(out,"Case #%d: %d %d\n",i+1, res1, res2);
	}
}