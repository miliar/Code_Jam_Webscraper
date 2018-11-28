/*Author:rednivrug15*/
#include<bits/stdc++.h>
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define ll long long
#define MOD 1000000007

long long power(long long a,long long b,long long mod)
{
    long long ret=1;

    while(b)
    {
        if(b%2==1)
            ret=(ret*a)%mod;
        b/=2;
        a=(a*a)%mod;
    }
    return ret;
}

int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}

int n,m;
char str[101][101];

bool issafe(int x,int y)
{
    if(x>=n || y>=m)
        return 0;
    if(x<0 || y<0)
        return 0;
    return 1;
}

vector < pii > dfsvisit;
int safety[101][101];
int hasacycle;
bool visited[101][101];

int decode(char x)
{
    if(x=='^')
        return 0;
    if(x=='v')
        return 1;
    if(x=='<')
        return 2;
    return 3;
}

char encode(int x)
{
    if(x==0)
        return '^';
    if(x==1)
        return 'v';
    if(x==2)
        return '<';
    return '>';
}

int xx,yy;
int changes;

void dfs(int x,int y,int lastx,int lasty)
{
    xx=lastx;
    yy=lasty;

    if(issafe(x,y)==0)
        return;

    if(safety[x][y]==1)
    {
        hasacycle=1;
        return;
    }

    if(visited[x][y]==1)
    {
        hasacycle=1;
        return;
    }

    if(str[x][y]!='.')
    {
        visited[x][y]=1;
        dfsvisit.pb(mp(x,y));
    }

    if(str[x][y]=='.')
    {
        if(str[lastx][lasty]=='^')
         dfs(x-1,y,lastx,lasty);
        else if(str[lastx][lasty]=='v')
            dfs(x+1,y,lastx,lasty);
        else if(str[lastx][lasty]=='<')
            dfs(x,y-1,lastx,lasty);
        else
            dfs(x,y+1,lastx,lasty);
    }

    else
    {
        if(str[x][y]=='^')
         dfs(x-1,y,x,y);
        else if(str[x][y]=='v')
            dfs(x+1,y,x,y);
        else if(str[x][y]=='<')
            dfs(x,y-1,x,y);
        else
            dfs(x,y+1,x,y);

        if(hasacycle==0)
        {
            int counts=1,start=decode(str[x][y]);

            while(hasacycle==0 && counts<4)
            {
                start=(start+1)%4;
                str[x][y]=encode(start);
                counts++;

                if(str[x][y]=='^')
                    dfs(x-1,y,x,y);
                else if(str[x][y]=='v')
                    dfs(x+1,y,x,y);
                else if(str[x][y]=='<')
                    dfs(x,y-1,x,y);
                else
                    dfs(x,y+1,x,y);
            }
        }

        if(hasacycle==1)
            return;
        else
        {
            visited[x][y]=0;
            dfsvisit.pop_back();
        }
    }
}

char strx[101][101];
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for(int test=1; test<=t; test++)
    {
        printf("Case #%d: ",test);
        scanf("%d%d",&n,&m);

        memset(safety,0,sizeof safety);
        memset(visited,0,sizeof visited);

        for(int i=0; i<n; i++)
            scanf("%s",str[i]);

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
             strx[i][j]=str[i][j];
        bool flag=0;
        int ans=0;

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(str[i][j]=='.')
                    continue;
                //printf("Fired from % %d--\n",i,j);
                int start=decode(str[i][j]);
                hasacycle=0;
                int chances=0;
                while(hasacycle==0 && chances<4)
                {
                    dfsvisit.clear();
                    dfs(i,j,i,j);

                    if(hasacycle==0)
                    {
                        str[i][j]=encode(start);
                        for(int x=0; x<dfsvisit.size(); x++)
                            visited[dfsvisit[x].first][dfsvisit[x].second]=0;
                    }
                    else
                        break;
                    chances++;
                }
                if(hasacycle==0)
                {
                    flag=1;
                    ans=-1;
                    break;
                }

                else
                {
                    for(int x=0; x<dfsvisit.size(); x++)
                     safety[dfsvisit[x].first][dfsvisit[x].second]=1;
                }
            }
            if(flag==1) break;
        }

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
            ans+=(strx[i][j]!=str[i][j]);

        // for(int i=0; i<n; i++)
           // printf("%s\n",str[i]);
        if(flag==1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",ans);
    }
    return 0;
}
