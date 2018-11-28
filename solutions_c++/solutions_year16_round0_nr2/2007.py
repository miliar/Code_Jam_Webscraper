#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main()
{
    freopen("QB.in","r",stdin);
    freopen("QB.out","w",stdout);
    int T,ans;
    string s;
    char ch;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        cin>>s;
        ch='+';
        ans=0;
        for(int i=s.size()-1;i>=0;i--)
            if(s[i]!=ch)
            {
                ans++;
                ch=s[i];
            }
        printf("Case #%d: %d\n",I,ans);
    }
}
