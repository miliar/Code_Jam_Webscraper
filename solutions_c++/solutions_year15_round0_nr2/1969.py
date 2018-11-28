# include <iostream>
# include <vector>
# include <cstring>
#include <stdio.h>
#include <set>
#include <algorithm>
using namespace std;
int a[1001];
int main()
{
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int tst=1;tst<=t;tst++)
    {
        int n;
        cin>>n;
        for (int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        int ans=10000;
        for (int i=1;i<=1000;i++)
        {
            int now=0;
            for (int j=0;j<n;j++)
            {
                if (i>=a[j])
                    continue;
                if (a[j]%i==0)
                    now+=a[j]/i - 1;
                else
                    now+=a[j]/i;
            }
            now+=i;
            ans=min(ans,now);
        }
        cout<<"Case #"<<tst<<": "<<ans<<endl;
    }
}
