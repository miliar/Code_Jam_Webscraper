#include<iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int p=1;p<=t;p++)
    {
        unsigned long long n;
        cin>>n;
        int a[10]={0};
        unsigned long long i=1;
        cout<<"Case #"<<p<<": ";
        if(n==0)
          cout<<"INSOMNIA\n";
        else
        {
          while(1)
          {
              unsigned long long temp=n*i;
              while(temp)
              {
                  int rem=temp%10;
                  a[rem]=1;
                  temp/=10;
              }
              int count=0;
              for(int j=0;j<10;j++)
              {
                  if(a[j])
                    count++;
              }
              if(count==10)
                  break;
              i++;
          }
          unsigned long long ans=n*i;
          cout<<ans<<"\n";
        }
    }
    return 0;
}
