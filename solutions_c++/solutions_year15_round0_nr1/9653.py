#include<bits/stdc++.h>
using namespace std;

char s[2005];
int main()
{
    int t,n;
    cin>>t;

    for(int tst=1;tst<=t;tst++)
    {
        cin>>n>>s;

        int totalAvailable = 0;
        int count = 0;
        for(int i = 0;i<=n;i++)
        {
            if(totalAvailable>=i)
            {
                totalAvailable += (s[i]-'0');
            }
            else
            {
                count = count + i -totalAvailable;
                totalAvailable = i + (s[i]-'0');
            }
        }
        printf("Case #%d: %d\n",tst,count);
    }
    return 0;
}
