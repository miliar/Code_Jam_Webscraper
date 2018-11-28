# include <iostream>
# include <vector>
# include <cstring>
#include <stdio.h>
#include <set>
#include <algorithm>
using namespace std;
int main()
{
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int tst=1;tst<=t;tst++)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int ans=0;
        int now=(int)s[0]-48;
        for (int i=1;i<=n;i++)
        {
            if (s[i]=='0')
                continue;
            if (now<i)
            {
                ans+=i-now;
                now+=i-now;
            }
            now+=(int)s[i]-48;
        }
        cout<<"Case #"<<tst<<": "<<ans<<endl;
    }
}
