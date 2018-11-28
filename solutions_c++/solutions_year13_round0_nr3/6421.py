#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<math.h>

using namespace std;
int main()
{
    int T,A,B,a,b,l;
    double c,d;
    cin>>T;
    int rev,j,i,dig;
    for(l=1;l<=T;l++)
    {
           int m=0,n,k;          
             cin>>A;
             cin>>B;
            c= sqrt(A);
             a=int(c);
             if(c>a)
             {
                   a=a+1;
                  
             }                    
            d= sqrt(B);
             b=int(d);
                                         
             
             
    for(i=a;i<=b;i++)
    {           
              n=i;
             j=i;
             rev=0;
             while(j>0)
             {
                       dig=j%10;
                       rev=rev*10+dig;
                       j=j/10;
             }
             if(n==rev)
             {          n=i*i;
                       k=i*i;
                       rev=0;
                       while(k>0)
                       {
                       dig=k%10;
                       rev=rev*10+dig;
                       k=k/10;
                       }
                       if(n==rev)
                       {
                         m++;
                        }
             }          
             
    }
        cout<<"Case #"<<l<<": "<<m<<endl; 
    
}             
    getche();
    return 0;
}    
         
    
