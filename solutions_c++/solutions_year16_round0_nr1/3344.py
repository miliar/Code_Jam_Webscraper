#include<iostream>
using namespace std;
int main()
{
    unsigned long long n,j,val;
    int t,i;
    int d,k,flag=0;
    cin>>t;
    for(i=1;i<=t;++i)
    {
    cin>>n;
    if(n==0)
    cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    else
    {
    int ar[10];
    for(k=0;k<10;++k)
    ar[k]=0;
    for(j=1;;++j)
    {
       val=n*j;
       flag=1;
       while(val!=0)
       {
          d=val%10;
          ++ar[d];
          val=val/10;          
       }
       for(k=0;k<10;++k)
       if(ar[k]==0)
       flag=0;
       if(flag==1)
       break;
    }        
    flag=0;
       for(k=0;k<10;++k)
       if(ar[k]==0)
       flag=1;
       if(flag!=1)
    cout<<"Case #"<<i<<": "<<n*j<<endl;
    }
    }
    return 0;
}

