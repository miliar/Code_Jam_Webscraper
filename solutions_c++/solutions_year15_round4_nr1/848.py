#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define ll long long
#define mod 1000000007LL
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vi vector<int>
#define vpii vector< pii >

int direction[][2]={ {0,0},{0,1},{0,-1},{1,0},{-1,0} };
map< char,int > dr;
int a[110][110],ans[5][110][110];
set< pair<int,int> > chg;


int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t,n,m,i,j,ans1,fg;
    char s[110];
    dr['.']=0;
    dr['^']=1;
    dr['v']=2;
    dr['>']=3;
    dr['<']=4;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d %d",&n,&m);
        ans1=0;
        for(i=0;i<110;i++)
        {
            for(j=0;j<110;j++)
            {
                for(int k=0;k<5;k++)
                    ans[k][i][j]=0;
            }
        }
        for(i=0;i<n;i++)
        {
            scanf("%s",s);
            for(j=0;j<m;j++)
            {
                a[i][j]=dr[s[j]];
            }
        }
        chg.clear();
        fg=0;
        for(i=0;i<n;i++)
        {
            j=0;
            while(a[i][j]==0&&j<m)    j++;
            ans[ 4 ][i][j]=1;
            if(a[i][j]==4&&j<m)
            {
                chg.insert( mp(i,j) );
                a[i][j]--;
            }
            j=m-1;
            while(j>=0&&a[i][j]==0)    j--;
            ans[ 3 ][i][j]=1;
            if(a[i][j]==3&&j>=0)
            {
                chg.insert( mp(i,j) );
                if(ans[ a[i][j]+1 ][i][j]==1)
                    a[i][j]--;
                else
                    a[i][j]++;
            }
        }
        for(j=0;j<m;j++)
        {
            i=0;
            while(a[i][j]==0&&i<n)    i++;
            ans[ 1 ][i][j]=1;
            if(a[i][j]==1&&i<n)
            {
                chg.insert( mp(i,j) );
                a[i][j]++;
            }
            i=n-1;
            while(i>=0&&a[i][j]==0)    i--;
            ans[ 2 ][i][j]=1;
            if(a[i][j]==2&&i>=0)
            {
                chg.insert( mp(i,j) );
                if(ans[ 1 ][i][j]==0)
                    a[i][j]=1;
                else
                {
                    if(ans[3][i][j]==0)
                        a[i][j]=3;
                    else if(ans[4][i][j]==0)
                        a[i][j]=4;
                    else
                    {
                        fg=1;
                        break;
                    }
                }
            }
        }
        if(fg)
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
            continue;
        }
        ans1=(int)chg.size();
        printf("Case #%d: %d\n",t,ans1);
    }
    return 0;
}
