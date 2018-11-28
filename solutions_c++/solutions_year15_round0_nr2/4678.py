#include <iostream>
#include<algorithm>
using namespace std;

int main() {
	long long int t,d,p[10005],i,res,cmp,pos=1,j;
    cin>>t;
    while(t--)
   {
   cin>>d;
   for(i=1;i<=d;i++)
     cin>>p[i];

   long long int maxi=p[1];
   for(i=1;i<=d;i++)
     if(p[i]>maxi)
        maxi=p[i];


   res=maxi;
   for(i=1;i<maxi;i++)
        {
           long long int nsu=0,maxx=0;
            for(j=1;j<=d;j++)
            {
                if(p[j]>i)
                {
                     nsu= nsu+(p[j] / i)-1;
                    if(p[j]%i)
                        nsu++;
                    maxx=max(maxx,i);
                }
                else
                    maxx=max(maxx,p[j]);
            }
            nsu=nsu+maxx;
            if(nsu<res)
                 res=nsu;
        }

   cout<<"Case #"<<pos<<": "<<res<<"\n";
   pos++;

   }
	return 0;
}
