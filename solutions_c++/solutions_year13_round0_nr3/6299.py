#include<iostream>
#include<cmath>
using namespace std;




long long isPal(long long x)
{
    long temp=x;
    long temp2=0;
    while(temp)
    {
               temp2=temp2*10+temp%10;
               temp=temp/10;
    }
    if(temp2==x)
    return 1;
    else return 0;
}

int main()
{
    long long t;
    cin>>t;
    long long cnt=0;
    while(cnt<t)
    {
                cnt++;
                long long a,b;
                cin>>a>>b;
                long long m=0;
                if(a>b)
                {long long c=b; b=a;a=c;}
                for(long long i=a;i<=b;i++)
                {
                        double y=sqrt(i);
                        long long z=(long long)y;
                        if((z-y==0)&&(isPal(z))&&(isPal(i)))
                        m++;
                }
                cout<<"Case #"<<cnt<<": "<<m<<endl;
                
    }
    
}
