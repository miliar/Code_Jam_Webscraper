#include<iostream.h>
#include<conio.h>
#include<stdio.h>

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("outp.in","w",stdout);

    
   long int i,j,l,m,count=0;
    
   long int a,b,k;
    
   long int n;
    cin>>n;
    for(m=0;m<n;m++)
    {
                    count=0;
                    cin>>a>>b>>k;
               for(i=0;i<a;i++)
               for(j=0;j<b;j++)
               {
                            long int x=(i&j);
                              // cout<<"x="<<x<<endl;
                               for(l=0;l<k;l++)
                               {
                                               if(l==x)
                                               count++;
                               }
               }  
               
               cout<<"Case #"<<m+1<<": "<<count<<"\n";   
                    
    }
    
   // getch();
   // return 0;
}
