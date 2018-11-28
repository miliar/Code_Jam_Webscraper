#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;


int r,c,m,tot,lef;

const int maxn = 51;

int mp[maxn][maxn];
int dx[8] = {-1,-1,0,1,1,1,0,-1};
int dy[8] = {0,1,1,1,0,-1,-1,-1};

int par[2505];

int findset(int x)
{
    if(par[x]!=x)
        par[x] = findset(par[x]);
    return par[x];
}

void unionset(int x,int y)
{
    int fx = findset(x);
    int fy = findset(y);
    par[fx] = fy;
}
bool zero(int x,int y)
{
    for(int i=0; i<8; i++)
    {
        int px = x + dx[i];
        int py = y + dy[i];
        if(1<=px&&px<=r&&1<=py&&py<=c&&mp[px][py]=='*')
            return 0;
    }
    return 1;
}
bool dfs(int p,int le)
{
    if(tot-p+1<le)
        return 0;
    if(le==0)
    {
        /*for(int i=1; i<=r; i++)
        {
            for(int j=1; j<=c; j++)
                putchar(mp[i][j]);
            putchar('\n');
        }*/
        for(int i=1; i<=tot; i++)
            par[i] = i;
        for(int i=1; i<=r; i++)
        {
            for(int j=1; j<=c; j++)
            {
                if(mp[i][j]=='.'&&zero(i,j))
                {
                    //printf("i=%d,j=%d\n",i,j);
                    for(int k=0; k<8; k++)
                    {
                        int px = i + dx[k];
                        int py = j + dy[k];
                        if(1<=px&&px<=r&&1<=py&&py<=c&&mp[px][py]=='.'&&zero(px,py))
                            unionset((px-1)*c+py,(i-1)*c+j);
                    }
                }
            }
        }
        for(int i=1; i<=r; i++)
        {
            for(int j=1; j<=c; j++)
            {
                if(mp[i][j]=='.'&&zero(i,j))
                {
                    for(int k=0; k<8; k++)
                    {
                        int px = i + dx[k];
                        int py = j + dy[k];
                        if(1<=px&&px<=r&&1<=py&&py<=c&&mp[px][py]=='.'&&zero(px,py)==0)
                        {
                            if(par[(px-1)*c+py]==(px-1)*c+py)
                                unionset((px-1)*c+py,(i-1)*c+j);
                        }
                    }
                }
            }
        }
        int cnt = 0,kr,kc;
        for(int i=1; i<=tot; i++)
        {
            if(par[i]==i)
            {
                cnt++;
                int pr = (i-1)/c+1;
                int pc = (i-1)%c+1;
                if(mp[pr][pc]=='.')
                {
                    kr=pr;
                    kc=pc;
                }
            }
        }
        //printf("cnt=%d\n",cnt);
        if(cnt==m+1)
        {
            mp[kr][kc] = 'c';
            for(int i=1; i<=r; i++)
            {
                for(int j=1; j<=c; j++)
                    putchar(mp[i][j]);
                putchar('\n');
            }
            return 1;
        }
        else
            return 0;
    }
    int pr = (p-1)/c+1;
    int pc = (p-1)%c+1;
    mp[pr][pc] = '*';
    if(dfs(p+1,le-1))
        return 1;
    mp[pr][pc] = '.';
    if(dfs(p+1,le))
        return 1;
    return 0;
}
bool solve()
{
    for(int i=1; i<=r; i++)
        for(int j=1; j<=c; j++)
            mp[i][j] = '.';
    if(dfs(1,m))
        return 1;
    return 0;
}
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d:\n",++cas);
        scanf("%d%d%d",&r,&c,&m);
        tot = r*c;
        lef = tot - m;
        if(r==1)
        {
            for(int i=0; i<m; i++)
                putchar('*');
            for(int i=0; i<lef-1; i++)
                putchar('.');
            putchar('c');
            putchar('\n');
            continue;
        }
        if(c==1)
        {
            for(int i=0; i<m; i++)
                printf("*\n");
            for(int i=0; i<lef-1; i++)
                printf(".\n");
            printf("c\n");
            continue;
        }
        int flag = 0,gr,gc;
        for(int i=2; i<=r; i++)
        {
            if(flag)
                break;
            for(int j=2; j<=c; j++)
            {
                if(i*j==lef)
                {
                    flag = 1;
                    gr = i;
                    gc = j;
                    break;
                }
            }
        }
        if(!flag)
        {
            if(!solve())
                puts("Impossible");
        }
        else
        {
            for(int i=1; i<=r; i++)
                for(int j=1; j<=c; j++)
                    mp[i][j] = '*';
            for(int i=1; i<=gr; i++)
                for(int j=1; j<=gc; j++)
                    mp[i][j] = '.';
            mp[1][1] = 'c';
            for(int i=1; i<=r; i++)
            {
                for(int j=1; j<=c; j++)
                    putchar(mp[i][j]);
                putchar('\n');
            }
        }
    }
}
