#include<iostream.h>
#include<conio.h>
#include<stdio.h>

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("outp.in","w",stdout);

    
long int i,j,t,m,c=0;
    
long int a,b,k;
    
long int n;
cin>>n;
for(m=0;m<n;m++)
{
c=0;
cin>>a>>b>>k;
for(i=0;i<a;i++)
for(j=0;j<b;j++)
               {
               long int x=(i&j);
                              
                               for(t=0;t<k;t++)
                               {
                                               if(t==x)
                                               c++;
                               }
               }  
               
               cout<<"Case #"<<m+1<<": "<<c<<"\n";   
                    
    }
    
   // getch();
   // return 0;
}
