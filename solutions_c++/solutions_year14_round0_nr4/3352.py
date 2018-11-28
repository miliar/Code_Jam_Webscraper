
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
FILE *fp_in,*fp_out;
int main(){
	int t,n,i,j,k=1;
	if((fp_in=fopen("D-large.IN","r"))==NULL)
		return 0;
	if((fp_out=fopen("out","w"))==NULL)
		return 0;
	double a[1005],b[1005];
	fscanf(fp_in,"%d",&t);
	while(t--){
		int y=0,z=0;
		fscanf(fp_in,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(fp_in,"%lf",&a[i]);
		for(i=0;i<n;i++)
			fscanf(fp_in,"%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		/*
		printf("%d:\n",k);
		for(i=0;i<n;i++)
			printf("%.4lf ",a[i]);
		printf("\n");
		for(i=0;i<n;i++)
			printf("%.4lf ",b[i]);
		printf("\n");
		*/
		i=0;j=0;
		int m=n;
		while(i<n&&j<m)
			if(a[i++]>b[j])
				y++,j++;
			else 
				m--;	
		for(i=0,j=0;i<n;i++){
			while(j<n)
				if(a[i]<b[j++])break;
			if(j>=n)break;
		}
		if(a[i]<b[n-1])i++;
		z=n-i;
		fprintf(fp_out,"Case #%d: %d %d\n",k++,y,z);
	}
	return 0;
}
