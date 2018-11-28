#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int t,n,ans,d[100][100],di[100];
string s[100],r[100];

int calc(int d[],int e)
{
    int i,j;
    for(i=j=0;i<n;i++)
        j+=abs(d[i]-e);
    return j;
}

int bis(int d[])
{
    int i,l,h;
    for(i=0,l=0x7fffffff,h=0;i<n;i++)
    {
        l=min(l,d[i]);
        h=max(l,d[i]);
    }
    for(i=0x7fffffff;l<=h;l++)
    {
        i=min(i,calc(d,l));
    }
    return i;
}

void init()
{
    int i,j,k,l;
    ans=0;
    for(i=0;i<n;i++)
    {
        cin>>s[i];
        r[i]=s[i];
    }
    for(i=0;i<n;i++)
    {
        for(j=1;j<s[i].length();j++)
        {
            while(j<s[i].length()&&s[i][j]==s[i][j-1])
                s[i].erase(j,1);
        }
    }
    for(i=1;i<n&&s[0]==s[i];i++);
    if(i<n)
    {
        ans=-1;
        return;
    }
    memset(di,0,sizeof di);
    for(i=0;i<s[0].length();i++)
    {
        for(j=0;j<n;j++)
        {
            for(k=di[j];k<r[j].length()&&r[j][k]==s[0][i];k++);
            d[i][j]=k-di[j];
            di[j]=k;
        }
    }
    for(i=0;i<s[0].length();i++)
    {
        ans+=bis(d[i]);
    }
}

void solve()
{
    printf("Case #%d: ",++t);
    if(ans==-1)
        puts("Fegla Won");
    else
        printf("%d\n",ans);
}

int main()
{
    scanf("%*d");
    while(~scanf("%d",&n))
    {
        init();
        solve();
    }
    return 0;
}
