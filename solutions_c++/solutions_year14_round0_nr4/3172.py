#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int t,cases=1;
	FILE *fp1,*fp2;
    fp1=fopen("D-large.in","r");
    fp2=fopen("output.txt","w");
	fscanf(fp1,"%d",&t);
	while(t--)
    {
		int N,deewar=0,war=0;
		double ken[1001],nmi[1001];

        fscanf(fp1,"%d",&N);
        for(int i=0;i<N;i++)
            fscanf(fp1,"%lf",&nmi[i]);
        for(int i=0;i<N;i++)
            fscanf(fp1,"%lf",&ken[i]);
        
		sort(nmi,nmi+N);
        sort(ken,ken+N);
		
		for(int i=0,j=0;j<N;j++)
            if(ken[j] > nmi[i])
            {
				war++;	
				i++;
			}
        for(int i=0,j=0;i<N;i++)
            if(nmi[i] > ken[j])
            {
				deewar++;	
				j++;
			}
		
		fprintf(fp2,"Case #%d: %d %d\n",cases,deewar,N-war);
		cases++;
    }
	return 0;
}