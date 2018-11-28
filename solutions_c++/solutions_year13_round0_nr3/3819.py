//By Ansuraj Khadanga
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;

int main()
{
    FILE *stream;
	if((stream=freopen("C-small-attempt0.in","r",stdin))==NULL)
		exit(-1);
	if((stream=freopen("A-large-practice.out","w",stdout))==NULL)
		exit(-1);
		
		int t,l,u,i,temp,sum,r,sq2,j,temp2,counter=0,k=1;
		double sq;
		cin>>t;
		while(t>0)
		{
                  cin>>l>>u;
           counter=0; 
  for(i=l;i<=u;i++)
    {
                  temp=i;
                  sum=0;

         while(temp)
         {
                    
             r=temp%10;
             temp=temp/10;
             sum=sum*10+r;
         }
         if(i==sum)   
         {    
                sq=sqrt(i);
                sq2=int(sq);
                
                if(sq2==sq)
            {
                temp2=sq2;
                j=0;
                   while(sq2)
                   {
              r=sq2%10;
             sq2=sq2/10;
             j=j*10+r;         
                   }
                   if(temp2==j)
                   {
                     counter++;
                   }
             }
         }
           
   }
          cout<<"Case #"<<k++<<": "<<counter; 
            t--;
            if(t>0)
            cout<<"\n";
        }
		
    return EXIT_SUCCESS;
}
