#include<iostream>
using namespace std;
int main()
{
    freopen("AB1.in","r",stdin);
	freopen("AB1.out","w",stdout);
	int i,j,t,a,b,k,res;
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
         res=0;
         cin>>a>>b>>k;
         for(i=0;i<a;i++)
         {
             for(j=0;j<b;j++)
             {
                    if((j&i)<k)
                    {
                        
                           res++;
                                            }
             }
         }
         cout<<"Case #"<<ii<<": "<<res<<"\n";
     }
	
}
