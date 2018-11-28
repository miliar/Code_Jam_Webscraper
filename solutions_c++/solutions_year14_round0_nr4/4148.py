#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int t,n=1,k;
	FILE *f1,*f2;
    f1=fopen("D-large.in","r");
    f2=fopen("output.txt","w");
	fscanf(f1,"%d",&t);
	for(k=0;k<t;k++)
    {
		int N,deewar=0,war=0;
		double ken[1001],nao[1001];

        fscanf(f1,"%d",&N);
        for(int i=0;i<N;i++)
            fscanf(f1,"%lf",&nao[i]);
        for(int i=0;i<N;i++)
            fscanf(f1,"%lf",&ken[i]);
        
		sort(nao,nao+N);
        sort(ken,ken+N);
		
		for(int i=0,j=0;j<N;j++)
            if(ken[j] > nao[i])
            {
				war++;	
				i++;
			}
        for(int i=0,j=0;i<N;i++)
            if(nao[i] > ken[j])
            {
				deewar++;	
				j++;
			}
		
		fprintf(f2,"Case #%d: %d %d\n",n,deewar,N-war);
		n++;
    }
	return 0;
}
