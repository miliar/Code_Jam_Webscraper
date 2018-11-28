#include<stdio.h>
#include<math.h>
#include<fstream>
using namespace std;
int arr[]={1,4,9,121,484};
int main()
{
	//ofstream myfile;
	//myfile.open("INPUT.txt");
	FILE *fp,*fp2;
	fp = fopen("C-small-attempt3.in","r");
	fp2 = fopen("attempt0.out","w");
	int t,a,b,i,j=1,n,alim,blim,count;
	fscanf(fp,"%d",&t);
	while(j<=t)
	{
		count=0;
		fscanf(fp,"%d",&a);
		fscanf(fp,"%d",&b);
		for(i=0;i<5;i++)
		{
			if(arr[i]>=a&&arr[i]<=b)
				count++;
		}
		fprintf(fp2,"Case #%d: %d\n",j,count);
		j++;
	}
	
	return 0;
}
