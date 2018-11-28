#include <stdio.h>
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
#define Min(a,b) ((a)>(b)?(b):(a))
int T,t;
int n,m,a[105][105],maxx[105],maxy[105],i,j,k;
int main(){
	for(fscanf(in,"%d",&T);T--;){
		fscanf(in,"%d%d",&n,&m);
		for(i=0;i<n;i++) for(j=0;j<m;j++) fscanf(in,"%d",&a[i][j]);
		for(i=0;i<n;i++) maxx[i]=a[i][0];
		for(j=0;j<m;j++) maxy[j]=a[0][j];
		for(i=0;i<n;i++) 
			for(j=0;j<m;j++){
				if(a[i][j]>maxx[i]) maxx[i]=a[i][j];
				if(a[i][j]>maxy[j]) maxy[j]=a[i][j];
			}
		int flag=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++){
				if(a[i][j]!=Min(maxx[i],maxy[j])) flag=1;
			}
		fprintf(out,"Case #%d: ",++t);
		if(flag==0) fprintf(out,"YES\n");
		else fprintf(out,"NO\n");
	}
	return 0;
}