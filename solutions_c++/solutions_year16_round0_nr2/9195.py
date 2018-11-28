#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++)
    {
        string s;
        cin>>s;
        int c=0;
        for(int i=1;i<s.length();i++)
        {
            if(s[i]!=s[i-1])
                c++;
        }
        if(s[s.length()-1]=='-')
            c++;
        printf("Case #%d: %d\n",tc,c);
    }
    return 0;
}
