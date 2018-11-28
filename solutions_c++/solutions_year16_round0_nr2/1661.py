#include<bits/stdc++.h>
using namespace std;
string str;
int cnt[105];

int solve(int x,int y)
{
    if(x<0)
        return 0;
    if(cnt[x]==x+1 && y==1)
        return 0;
    if(cnt[x]==x+1 && y==0)
        return 1;
    if(cnt[x]==(-x-1) && y==0)
        return 0;
    if(cnt[x]==(-x-1) && y==1)
        return 1;
    if(str[x]=='+' && y==1)
        return solve(x-1,y);
    if(str[x]=='+' && y==0)
        return solve(x-1,!y)+1;
    if(str[x]=='-' && y==1)
        return solve(x-1,!y)+1;
    if(str[x]=='-' && y==0)
        return solve(x-1,y);
}

int t,X,n,i,ans;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);

    while(t--)
    {
        X++;
        printf("Case #%d: ",X);
        cin>>str;
        n=str.length();

        cnt[0]=(str[0]=='+')?1:-1;

        for(i=1; i<n; i++)
            cnt[i]=cnt[i-1]+(str[i]=='+')?1:-1;

        i=n-1;

        while(i>=0 && str[i]=='+')
            i--;

        if(i<0)
            printf("0\n");
        else
        {
            ans=solve(i-1,0)+1;
            printf("%d\n",ans);
        }
    }
    return 0;
}
