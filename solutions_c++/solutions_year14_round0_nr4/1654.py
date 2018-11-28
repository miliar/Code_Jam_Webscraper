#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
double A[1001],B[1001];
int main()  
{
	FILE *fin,*fout;
	fin=fopen("D-large.in","rb");
	fout=fopen("D-large.out","wb");
	int r,t,i,n,dwar,war,j;
	fscanf(fin,"%d",&t);
	for(r=1;r<=t;r++)
	{
		fscanf(fin,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(fin,"%lf",A+i);
		for(i=0;i<n;i++)
			fscanf(fin,"%lf",B+i);
		sort(A,A+n);
		sort(B,B+n);
		dwar=0;
		i=n-1;
		for(j=n-1;j>=0;j--)
			if(A[i]>B[j])
			{
				dwar++;
				i--;
			}
		i=0;
		war=0;
		for(j=0;j<n;j++)
			if(A[i]<B[j])
			{
				war++;
				i++;
			}
		war=n-war;
		fprintf(fout,"Case #%d: %d %d\n",r,dwar,war);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}