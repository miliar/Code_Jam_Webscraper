#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;

int pal(int x)
{
int p=0;     
int q=x;
while(x>0)
{
p*=10;
p+=x%10;
x/=10;              
}     

if(p==q)
p=1;
else 
p=0;

return p;
}

int main()
{
ofstream cout("output.txt");
int a,b,n,t,m;
int c[150];
cin>>t;
int d=1;
while(d<=t)
{
cin>>a>>b;
m=(int)sqrt(a);          
n=m*m;

if(n<a)
{
n+= 2*m+1;
m++;
}

c[d]=0;

             while(n<=b)
             {    
             if((pal(m))&&(pal(n)))
             {
             c[d]++;                     
             }
             n+= 2*m+1;
             m++;      
             }                
d++;          
}       

for(int i=1;i<=t;i++)
        cout<<"Case #"<<i<<": "<<c[i]<<endl; 
}
