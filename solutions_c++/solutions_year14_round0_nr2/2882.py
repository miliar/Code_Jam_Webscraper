#include<iostream>
#include<iomanip>
#include<cstdio>
using namespace std;
int main()
{
    freopen("B1.in","r",stdin);
	freopen("B1.out","w",stdout);
	int t,ii;
	double c,f,x,nf,cost,min_cost,fixed;
	cin>>t;
	for(ii=1;ii<=t;ii++)
	{
         cin>>c>>f>>x;
         cost=x/2;
         min_cost=cost;
         nf=2;
         fixed=0;
         while(1)
         {
             fixed+=c/nf;
             nf=nf+f;
             cost=fixed+x/nf;
             if(cost<min_cost)
                 min_cost=cost;
             else
                 break;
         }
         cout<<"Case #"<<ii<<": "<<std::fixed<<setprecision(7)<<min_cost<<"\n";
    }
}
                     
