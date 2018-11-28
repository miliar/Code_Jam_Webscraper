#include<stdio.h>

int a[7]={1,4,9,121,484};
int main()
{
	FILE *in=fopen("C-small-attempt0.in","r");
	FILE *out=fopen("C-small-attempt0.out","w");
	int t,x,y,i,j,k,l,cnt;

	fscanf(in,"%d",&t);
	for(i=0;i<t;i++){
		fscanf(in,"%d %d",&x,&y);
		cnt=0;
		for(j=4;j>=0;j--){
			if(x>a[j]) break; 
		} j++;
		for(k=0;k<5;k++){
			if(y<a[k]) break;
		} k--;
		for(l=j;l<=k;l++)
			cnt++;
		fprintf(out,"Case #%d: %d\n",i+1,cnt);
	}
	
	return 0;
}