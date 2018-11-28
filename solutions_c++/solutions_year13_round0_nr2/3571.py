#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//		#define out stdout
//		#define in stdin

int main(void)
{
#ifndef in
	FILE *in;
	in=fopen("B-large.in","rt");
	if(in==NULL){
		printf("\a");
		return -1;
	}
#endif
#ifndef out
	FILE *out;
	out=fopen("b.txt","wt");
	if(out==NULL){
		printf("\a");
		return -1;
	}
#endif
	
	int num[105][105];
	char wrong[105][105];
	int t,T,i,j,N,M,max,ans;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;++t){
		fprintf(out,"Case #%d: ",t);
		fscanf(in,"%d%d",&N,&M);
		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				fscanf(in,"%d",&num[i][j]);
		for(i=0;i<N;++i){
			max=0;
			for(j=0;j<M;++j){
				if(num[i][j]>max)
					max=num[i][j];
			}
			for(j=0;j<M;++j){
				if(num[i][j]<max)
					wrong[i][j]=1;
				else
					wrong[i][j]=0;
			}	
		}
				
		ans=1;
		for(j=0;j<M;++j){
			max=0;
			for(i=0;i<N;++i){
				if(num[i][j]>max)
					max=num[i][j];
			}
			for(i=0;i<N;++i){
				if(num[i][j]==max)
					wrong[i][j]=0;
				if(wrong[i][j]){
					ans=0;
				}
			}	
			if(!ans)
				break;
		}
			
		if(ans)
			fprintf(out,"YES\n");
		else
			fprintf(out,"NO\n");
	}

#ifndef in
	fclose(in);
#endif
#ifndef out
	fclose(out);
#endif
	return 0;
}

