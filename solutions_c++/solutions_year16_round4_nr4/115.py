#include<bits/stdc++.h>
using namespace std;


int mat[5][5];
int mb[5][5];
int ps[20];
int a[5];
bool wok[5];
bool dfs(int s,int n)
{
    if(s==-1)
        return 1;
    else
    {
        int has=0;
        for(int i=0;i<n;i++)
            if(mb[a[s]][i]&&wok[i]==0)
            {
                has=1;
                wok[i]=1;
                if(dfs(s-1,n)==0)return 0;
                wok[i]=0;
            }
        return has;
    }
}
bool ok(int n)
{
    for(int i=0;i<n;i++)
        a[i]=i;
    do
    {
        memset(wok,0,sizeof(wok));
        if(dfs(n-1,n)==0)return 0;
    }while(next_permutation(a,a+n));
    return 1;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int n;scanf("%d",&n);
        int pk=0;
        for(int i=0;i<n;i++)
        {
            char s[6];
            scanf("%s",s);
            for(int j=0;j<n;j++)
            {
                mat[i][j]=s[j]=='1';
                if(mat[i][j]==0)ps[pk++]=i*10+j;
            }
        }
        printf("Case #%d: ",ti++);
        for(int i=0;i<=pk;i++)
        {
            int has=0;
            if(i)
            {
                for(int s=(1<<i)-1,u=1<<pk;s<u;)
                {
                    memcpy(mb,mat,sizeof(mb));
                    for(int j=0;j<pk;j++)
                        if((1<<j)&s)
                            mb[ps[j]/10][ps[j]%10]=1;
                    if(ok(n))
                    {
                        printf("%d\n",i);
                        has=1;
                        break;
                    }
                    int b=s&-s;
                    s=(s+b)|(((s^(s+b))>>2)/b);
                }
            }
            else
            {
                memcpy(mb,mat,sizeof(mb));
                if(ok(n))
                {
                    printf("%d\n",i);
                    has=1;
                }
            }
            if(has)break;
        }
    }
    return 0;
}
