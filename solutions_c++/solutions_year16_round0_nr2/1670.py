#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        char a[105];
        scanf("%s",a);
        vector<char>s;
        s.pb(a[0]);
        for(int i=1;i<strlen(a);i++)
        {
            if(s.back()!=a[i])s.pb(a[i]);
        }
        int ans=0;
        if(s[0]=='-')ans++;
        for(int i=1;i<s.size();i++)
        {
            if(s[i]=='-')ans+=2;
        }
        printf("Case #%d: %d\n",ca,ans);
    }

    return 0;

}
