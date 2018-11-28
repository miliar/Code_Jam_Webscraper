#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;cin>>t;
    for(int j=1;j<=t;++j)
    {
        string s;cin>>s;
        int i,n=s.length(),k=0;
        for(i=0;i<n;++i)
        {
            if(s[i]=='+')
            {
                if(i && s[i-1]=='-')k++;
                if(i<n-1 && s[i+1]=='-')k++;
            }
        }
        printf("Case #%d: %d\n",j,k+(s[n-1]=='-'));
    }
    return 0;
}
