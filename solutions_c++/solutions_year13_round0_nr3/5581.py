#include<iostream>
#include<cstdlib>
#include<cmath>
using namespace std;
string ia(int j,string x)
{
       int k=0;
       x="";
       while(j!=0)
       {
          x+=j%10;
          j/=10;
       }
       return string ( x.rbegin(), x.rend() );
}
           
int main()
{
    int n,a,b,j,i,r,f1,c,k;
    cin>>n;
    string x,y;
    for(i=1;i<=n;i++)
    {
            
         cin>>a>>b;
         c=0;f1=0;
         for(k=a;k<=b;k++)
         {
              j=k;            
              x=ia(j,x);
              y=x;
              x=string ( x.rbegin(), x.rend() ); 
              if(x==y){
              f1=1;
              //cout<<x<<" "<<y<<endl;
              }
              else
              continue;
              if(f1==1)
              {
                       
                       r=sqrt(j);
                       if((r*r)==j){
                       x=ia(r,x);
                       y=x;
                       x=string ( x.rbegin(), x.rend() ); 
                       if(y==x){
                       f1=2;
                       }
                       }
                       else
                       continue;
              }
              if(f1==2)
              c++;
         }
         cout<<"Case #"<<i<<": "<<c<<endl; 
         }
}
                       
              
                            
