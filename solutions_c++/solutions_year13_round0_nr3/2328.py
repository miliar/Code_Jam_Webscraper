#include<iostream>
using namespace std;
bool pal(long long a)
{
     long long n=a,p=0;
     while(n)
     {
             p=p*10+n%10;
             n/=10;
     }
     return p==a;
}
long long d[10000001];
int main()
{
    int cnt=0;
    for(long long i=1 ; i<=10000000 ; ++i)
    {
            if(pal(i) && pal(i*i))
            {
             d[cnt]=i*i;
             ++cnt;
            }
    }
    int tc;
    cin>>tc;
    int cc=0;
    while(tc--)
    {
               ++cc;
               long long a,b;
               cin>>a>>b;
               int sum=0;
               for(int i=0 ; i<cnt ; ++i)
               {
                       if(d[i]>=a && d[i]<=b)
                       ++sum;
               }
               cout<<"Case #"<<cc<<": "<<sum<<endl;
    }
}
