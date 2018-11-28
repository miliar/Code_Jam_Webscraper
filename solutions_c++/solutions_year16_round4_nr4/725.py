#define N (1<<2)
#include <bits/stdc++.h>

using namespace std;

bool used[N];
char s[N][N+1];
int T,n,cas,p[N],f[N][N];

int calc(int st)
{
    int cnt=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        {
            if(st&(1<<(i*n+j))) f[i][j]=1;
            else f[i][j]=0;
        }
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(s[i][j]=='1' && !f[i][j]) return -1;
            else if(s[i][j]=='0' && f[i][j]) cnt++;
    return cnt;
}

bool dfs(int k)
{
    int cnt=0;
    if(k==n) return 1;
    for(int i=0;i<n;i++)
        if(f[p[k]][i] && !used[i])
        {
            cnt++,used[i]=1;
            int res=dfs(k+1);

            used[i]=0;
            if(!res) return 0;
        }
    return cnt>0;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    for(cin>>T;T--;)
    {
        cin>>n;
        for(int i=0;i<n;i++)
            scanf("%s",s[i]);

        int res=20;
        for(int i=0;i<(1<<(n*n));i++)
        {
            int cost=calc(i);
            if(cost==-1) continue;
            for(int j=0;j<n;j++)
                p[j]=j;
            bool flag=1;
            do
            {
                memset(used,0,sizeof(used));
                if(!dfs(0))
                {
                    flag=0;
                    break;
                }
            }while(next_permutation(p,p+n));
            if(flag)
                res=min(res,cost);
        }
        printf("Case #%d: %d\n",++cas,res);
    }
    return 0;
}
