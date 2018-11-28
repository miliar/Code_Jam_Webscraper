#include <iostream>

using namespace std;

int main()
{
    long long t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
       long long int k,c,s;
       cin>>k;
       cin>>c;
       cin>>s;
       cout<<"Case #"<<i<<": ";
       if(s<k-1)
       {
          cout<<"IMPOSSIBLE"<<endl;
       }
       else
       {
          if(k==1)
          {
            cout<<"1"<<endl;
            continue;
          }
          if(c==1 && s<k)
          {
             cout<<"IMPOSSIBLE"<<endl;
             continue;
          }
          else if(c==1)
          {
              cout<<"1 ";
          }
          for(int l=2;l<=k;l++)
          {
              cout<<l<<" ";
          }
          cout<<endl;
       }
    }
}
