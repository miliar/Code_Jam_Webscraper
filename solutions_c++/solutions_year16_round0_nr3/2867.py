#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;
unsigned long long j;
unsigned long long fast_pow(unsigned long long base, unsigned long long n) 
{
    if(n==0)
       return 1;
    if(n==1)
    return base;
    long long halfn=fast_pow(base,n/2);
    if(n%2==0)
        return ( halfn * halfn );
    else
        return ( ( ( halfn * halfn )  ) * base );
}
unsigned long long isPrime(unsigned long long n){
    unsigned long long i,t;
    for(i=2;i<=sqrt(n);++i)
    if(n%i==0)
    {
              return i;
}
    return 1;
}
void func(int a[100],int n,int pos,int flags)
{
     int i,k,flag=0,m,t;
     unsigned long long val=0,temp[11];
     for(i=2;i<=10;++i)
     {
     val=0;
     for(k=0;k<n;++k)
     {
       val=val+a[k]*fast_pow(i,n-1-k); 
     }
     temp[i]=isPrime(val);
     if(temp[i]==1)
     {
     flag=1;
     goto end;                 
     }
     }
     end:
     if(flag==0 && flags!=0)
     {          
                for(i=0;i<n;++i)
                cout<<a[i];
                for(i=2;i<=10;++i)
                cout<<" "<<temp[i];
                cout<<endl;
                j=j-1;
     }
     if(pos<n-1 && j>0)
     {
     func(a,n,pos+1,0);
     int b[100];
     for(i=0;i<n;++i)
     b[i]=a[i];
     b[pos]=1;
     func(b,n,pos+1,1);
     }
 }
int main()
{
    unsigned long long max = fast_pow(10,17);
    unsigned long long i;
    int n,t;
    cin>>t;
    cin>>n>>j;
    cout<<j<<endl;
    cout<<"Case #1: "<<endl;
    int a[n];
    for(i=0;i<n;++i)
    a[i]=0;
    a[0]=1;
    a[n-1]=1;
    func(a,n,1,1);
    cout<<"OVER"<<endl;
    cin>>t;
    return 0;
}
