#include<cstdio>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;
int x[1005];
int main()
{
    freopen("2015_Q_A_l.in","r",stdin);
    freopen("2015_Q_A_l.out","w",stdout);
    int T,ans,n;
    string s;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d",&n);
        cin>>s;
        for(int i=0;i<=n;i++)
            x[i]=s[i]-'0';
        ans=0;
        for(int i=1;i<=n;i++)
        {
            if(x[i-1]<i)
            {
                ans+=i-x[i-1];
                x[i-1]=i;
            }
            x[i]+=x[i-1];
        }
        printf("Case #%d: %d\n",I,ans);
    }
}
