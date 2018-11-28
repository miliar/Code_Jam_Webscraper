#include <bits/stdc++.h>
#define LL long long

using namespace std;

const int maxn = 10000 + 10;

using namespace std;
string ans[maxn];
int N,P,S,R;

void output()
{
    printf(" ");
    cout<<ans[1];
    printf("\n");
}

bool ok()
{
    int s=0,r=0,p=0;
    for (int i=0; i<1<<N; i++)
    {
        if (ans[1][i]=='P') p++;
        if (ans[1][i]=='S') s++;
        if (ans[1][i]=='R') r++;
    }
    if (p==P && s==S && r==R) return 1;
    return 0;
}

void dfs(int x,int c,int step)
{
    if (step==N)
    {
        if (x==0) ans[c]="P";
        if (x==1) ans[c]="R";
        if (x==2) ans[c]="S";
        return;
    }
    if (x==0)
    {
        dfs(0,2*c,step+1);
        dfs(1,2*c+1,step+1);
    }
    else if (x==1)
    {
        dfs(2,2*c,step+1);
        dfs(1,2*c+1,step+1);
    }
    else if (x==2)
    {
        dfs(0,2*c,step+1);
        dfs(2,2*c+1,step+1);
    }
    if (ans[2*c]<ans[2*c+1]) ans[c]=ans[2*c]+ans[2*c+1];
    else ans[c]=ans[2*c+1]+ans[2*c];
}

void work()
{
    scanf("%d%d%d%d",&N,&R,&P,&S);
    //printf("%d",1<<N);
    dfs(1,1,0);
    //cout<<ans[1]<<endl;
    if (ok()) {output(); return ;}
    dfs(0,1,0);
    //cout<<ans[1]<<endl;
    if (ok()) {output(); return ;}
    dfs(2,1,0);
    //cout<<ans[1]<<endl;
    if (ok()) {output(); return ;}
    printf(" IMPOSSIBLE\n");
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, cas = 0 ;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d:",++cas);
        work();
    }
    return 0;
}
