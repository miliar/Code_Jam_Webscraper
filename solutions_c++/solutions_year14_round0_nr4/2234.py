#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int t,h=1;
	FILE *fp1,*fp2;
    fp1=fopen("D-large.in","r");
    fp2=fopen("output.txt","w");
	fscanf(fp1,"%d",&t);
	while(t--)
    {
		int n,dwar=0,war=0;
		double ken[1001],naomi[1001];
        fscanf(fp1,"%d",&n);
        for(int i=0;i<n;i++)
            fscanf(fp1,"%lf",&naomi[i]);
        for(int i=0;i<n;i++)
            fscanf(fp1,"%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        for(int i=0,j=0;i<n;i++)
            if(naomi[i] > ken[j])
            {
				dwar++;	
				j++;
			}
		for(int i=0,j=0;j<n;j++)
            if(ken[j] > naomi[i])
            {
				war++;	
				i++;
			}
		fprintf(fp2,"Case #%d: %d %d\n",h,dwar,n-war);
		h++;
    }
	return 0;
}