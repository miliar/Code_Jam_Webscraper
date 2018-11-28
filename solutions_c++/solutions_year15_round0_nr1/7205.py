#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int k=0;k<n;k++)
    {
        int m;
        scanf("%d",&m);
        string s;
        cin>>s;
        int num[s.length()];
        for(int i=0;i<s.length();i++)
            num[i]=s[i]-'0';
        int tmp=0,ans=0;
        for(int i=0;i<s.length();i++)
        {
            if(num[i])
            {
                if(tmp<i)
                {
                    int d=i-tmp;
                    ans+=d;
                    tmp+=d+num[i];
                }
                else
                {
                    tmp+=num[i];
                }
            }
        }
        printf("Case #%d: %d\n",k+1,ans);
    }
}
