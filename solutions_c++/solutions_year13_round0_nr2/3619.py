#include<stdio.h>

int max1[101],max2[101];
int a[101][101];

int max(int x,int y){
	if(x>y) return x;
	return y;
}

int main()
{
	FILE *in=fopen("B-large.in","r");
	FILE *out=fopen("B-large.out","w");
	int t,i,j,k,m,n,chk;

	fscanf(in,"%d",&t);
	for(i=0;i<t;i++){
		chk=0;
		fscanf(in,"%d %d",&m,&n);
		for(j=0;j<m;j++){
			for(k=0;k<n;k++){
				fscanf(in,"%d",&a[j][k]);
				max2[k]=0;
			}
			max1[j]=0;
		}
		for(j=0;j<m;j++){
			for(k=0;k<n;k++){
				max1[j]=max(max1[j],a[j][k]);
				max2[k]=max(max2[k],a[j][k]);
			}
		}
		for(j=0;j<m;j++){
			for(k=0;k<n;k++){
				if(a[j][k]!=max1[j] && a[j][k]!=max2[k]) chk=1;
			}
		}
		fprintf(out,"Case #%d: ",i+1);
		if(chk == 1)
			fprintf(out,"NO\n");
		else 
			fprintf(out,"YES\n");
	}
	return 0;
}