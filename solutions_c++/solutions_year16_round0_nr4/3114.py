#include<bits/stdc++.h>
using namespace std;
int main()
{
      int t,k,c,s,o=0;
      cin>>t;
      while(t--)
      {o++;
            cin>>k>>c>>s;
            long long int tmp=ceil(pow(k,c-1));
            int i=1;
            cout<<"Case #"<<o<<": ";
            while(s)
            {
                  cout<<i<<" ";
                  i+=tmp;
                  s--;
            }
            cout<<"\n";
      }
}