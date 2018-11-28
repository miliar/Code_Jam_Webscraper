#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    int n;
    string s;
    for(int tt=1;tt<=t;tt++)
    {
      cin>>s;
      n=s.length();
      int fl=0;
      int ind;
      for(int i=n-1;i>=0;i--)
      {
          if(s[i]=='-')
            {
                fl=1;

                ind=i;
                break;
            }
      }

      if(fl==0)
        cout<<"Case #"<<tt<<": 0"<<endl;
        else
        {
           int cnt=1;
            fl=0;
           for(int j=ind;j>=0;j--)
            {
               if(s[j]=='-')
               {
                   if(fl!=0)
                   {
                       cnt++;
                       fl=0;
                   }
               }
               else
               {
                   if(fl==0)
                   {
                       cnt++;
                       fl=1;
                   }
               }
            }
            cout<<"Case #"<<tt<<": "<<cnt<<endl;
        }
    }
}
