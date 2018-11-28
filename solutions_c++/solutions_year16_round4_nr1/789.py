#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define pli pair<ll,int>
#define pil pair<int,ll>
#define pll pair<ll,ll>
#define all(v) v.begin(),v.end()
#define inf 1000000000
vector<int>s[100];
string func(string an,int n)
{
    int i,j,k;
    for(i=0;i<n;i++)
    {
        string ans="";
        for(k=0;k<(1<<n);k+=(1<<(i+1)))
        {
            string s="",h="";
            for(j=k;j<k+(1<<i);j++)
                s+=an[j],h+=an[j+(1<<i)];
            if(s<h)
                ans+=(s+h);
            else
                ans+=(h+s);
            //cout<<ans<<endl;
        }
        an=ans;
    }
    return an;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1-out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,j,k,flag=0,r,p,s1,c1,c2,c3;
        scanf("%d %d %d %d",&n,&r,&p,&s1);
        string ans="";
        s[0].clear();
        s[0].pb(1);
        for(i=1; i<=n; i++)
        {
            s[i].clear();
            for(j=0; j<s[i-1].size(); j++)
            {
                if(s[i-1][j]==1)
                {
                    s[i].pb(1);
                    s[i].pb(3);
                }
                if(s[i-1][j]==2)
                {
                    s[i].pb(2);
                    s[i].pb(1);
                }
                if(s[i-1][j]==3)
                {
                    s[i].pb(2);
                    s[i].pb(3);
                }
            }
        }
        c1=c2=c3=0;
        for(i=0; i<s[n].size(); i++)
            if(s[n][i]==1)
                c1++;
            else if(s[n][i]==2)
                c2++;
            else if(s[n][i]==3)
                c3++;
        if(c1==r&&c2==p&&c3==s1)
        {
            string an="";
            for(i=0; i<s[n].size(); i++)
                if(s[n][i]==1)
                    an+='R';
                else if(s[n][i]==2)
                    an+='P';
                else if(s[n][i]==3)
                    an+='S';
            flag=1;
            an=func(an,n);
            if(an<ans||(ans==""))
                ans=an;
        }
        s[0].clear();
        s[0].pb(2);
        for(i=1; i<=n; i++)
        {
            s[i].clear();
            for(j=0; j<s[i-1].size(); j++)
            {
                if(s[i-1][j]==1)
                {
                    s[i].pb(1);
                    s[i].pb(3);
                }
                if(s[i-1][j]==2)
                {
                    s[i].pb(2);
                    s[i].pb(1);
                }
                if(s[i-1][j]==3)
                {
                    s[i].pb(2);
                    s[i].pb(3);
                }
            }
        }
        c1=c2=c3=0;
        for(i=0; i<s[n].size(); i++)
            if(s[n][i]==1)
                c1++;
            else if(s[n][i]==2)
                c2++;
            else if(s[n][i]==3)
                c3++;
        if(c1==r&&c2==p&&c3==s1)
        {
            string an="";
            for(i=0; i<s[n].size(); i++)
                if(s[n][i]==1)
                    an+='R';
                else if(s[n][i]==2)
                    an+='P';
                else if(s[n][i]==3)
                    an+='S';
            flag=1;
            an=func(an,n);
            if(an<ans||(ans==""))
                ans=an;
        }
        s[0].clear();
        s[0].pb(3);
        for(i=1; i<=n; i++)
        {
            s[i].clear();
            for(j=0; j<s[i-1].size(); j++)
            {
                if(s[i-1][j]==1)
                {
                    s[i].pb(1);
                    s[i].pb(3);
                }
                if(s[i-1][j]==2)
                {
                    s[i].pb(2);
                    s[i].pb(1);
                }
                if(s[i-1][j]==3)
                {
                    s[i].pb(2);
                    s[i].pb(3);
                }
            }
        }
        c1=c2=c3=0;
        for(i=0; i<s[n].size(); i++)
            if(s[n][i]==1)
                c1++;
            else if(s[n][i]==2)
                c2++;
            else if(s[n][i]==3)
                c3++;
        if(c1==r&&c2==p&&c3==s1)
        {
            string an="";
            for(i=0; i<s[n].size(); i++)
                if(s[n][i]==1)
                    an+='R';
                else if(s[n][i]==2)
                    an+='P';
                else if(s[n][i]==3)
                    an+='S';
            flag=1;
            an=func(an,n);
            if(an<ans||(ans==""))
                ans=an;
        }

        printf("Case #%d: ",cs);
        if(flag==1)
            cout<<ans;
        else
            printf("IMPOSSIBLE");
        printf("\n");
        cs++;
    }
    return 0;
}
