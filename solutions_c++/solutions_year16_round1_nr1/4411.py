#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
    freopen("in-large","r",stdin);
    freopen("out","w",stdout);


    int t;
    string str;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
      cin>>str;
      string ans;
      ans+=str[0];
      for(int i=1;i<str.size();i++)
        {
           if(str[i]>=ans[0])
           {
             ans=str[i]+ans;
           }
            else
            {
             ans+=str[i];
            }

        }
        cout<<ans<<endl;
    }
    return 0;
}
