#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;
// sort using a custom function object
    struct {
        bool operator()(double a, double b)
        {   
            return a > b;
        }   
    } customLess;
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	int T;
	scanf("%d",&T);
	
	int Cas = 1;

	
	while (T-- >0)
	{
		int a,b,n;
		std::vector<double> Ken,Naomi;
		double tmp=0;
		a=b=0;
		
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			scanf("%Lf",&tmp);
			Naomi.push_back(tmp);
		}
		for (int i=0;i<n;i++)
		{
			scanf("%Lf",&tmp);
			Ken.push_back(tmp);
			
		}

		std::sort(Ken.begin(),Ken.end());
		std::sort(Naomi.begin(),Naomi.end());
		
	   int p=0;
       
       for(int j=0;j<n;j++)
       {                
           for (int k=p;k<n; k++)
           {
               if(Naomi[j]>Ken[k])
               {
                   p=k+1;
                   a++;
                   break;
               }
           }
       }
       p=0;
       for(int j=0;j<n;j++)
       {                
           for (int k=p;k<n; k++)
           {
               if(Ken[j]>Naomi[k])
               {
                   p=k+1;
                   b++;
                   break;
               }
           }
       }

			
		
		printf("Case  #%d: %d %d\n",Cas,a,n-b);
		
		Cas++;
	}
	return 0;
}