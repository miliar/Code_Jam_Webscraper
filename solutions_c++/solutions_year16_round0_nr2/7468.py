#include<iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int p=1;p<=t;p++)
    {
        string s;
        cin>>s;
        int n=s.size();
        int a[n+1];
        a[0]=1;
        for(int i=0;i<n-1;i++)
        {
          if(s[i+1]!=s[i])
            a[i+1]=a[i]+1;
          else
            a[i+1]=a[i];
        }
        cout<<"Case #"<<p<<": ";
        if(s[n-1]=='+')
          a[n-1]--;
        cout<<a[n-1]<<"\n";
      }
      return 0;
}
