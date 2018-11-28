#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;int x=1;
    while(t--)
    {

        int n;
        cin>>n;
        map <int,int> mp;

        for(int i=0;i<2*n-1;i++)
        {int a;
            for(int j=0;j<n;j++)
            {
                cin>>a;
            mp[a]++;}
        }
        cout<<"Case #"<<x<<": ";
        x++;
        for (int i=0;i!=mp.size();i++)
      {

          if(mp[i]%2==1)
            cout<<i<<" ";
      }
      cout<<"\n";
    }
}
