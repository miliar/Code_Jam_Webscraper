#include <bits/stdc++.h>
using namespace std;

const int maxn=5;

int n;
int a[maxn][maxn];
int b[maxn][maxn];
int w[maxn];
int u[maxn];
string s[maxn];

bool go(int p)
{
    if(p==n) return true;
    bool ok=true;
    bool was=false;
    for(int i=0;i<n;++i)
    {
        if(u[i]) continue;
        if(b[w[p]][i]==0) continue;
        was=true;
        u[i]=1;
        ok&=go(p+1);
        u[i]=0;
    }
    return ok && was;
}

bool test()
{
    memset(u,0,sizeof(u));
    return go(0);
}

bool check()
{
    for(int i=0;i<n;++i)
        w[i]=i;
    int cnt=1;
    for(int i=2;i<=n;++i) cnt*=i;
    bool ok=true;
    ok &= test();
    for(int i=0;i<cnt;++i)
    {
        next_permutation(w,w+n);
        ok &= test();
    }
    return ok;
}

int main()
{
    ios::sync_with_stdio(0);
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int T;
    //scanf("%d",&T);
    cin >> T;
    for(int test=1;test<=T;++test)
    {
        //printf("Case #%d: ", test);
        cout << "Case #" << test << ": ";
        cin >> n;
        for(int i=0;i<n;++i) cin >> s[i];
        for(int i=0;i<n;++i)for(int j=0;j<n;++j) a[i][j]=s[i][j]-'0';
        int m=0;
        int p=1;
        for(int i=0;i<n;++i)for(int j=0;j<n;++j)
        {
            if(a[i][j]) m+=p;
            p*=2;
        }
        m = (((1<<(n*n))-1)^m);
        int ans=n*n;
        for (int s=m; ; s=(s-1)&m)
        {
            p=1;
            int c=0;
            memset(b,0,sizeof(b));
            for(int i=0;i<n;++i)
            for(int j=0;j<n;++j)
            {
                b[i][j]=a[i][j];
                if(s&p) b[i][j]=1, c++;
                p*=2;
            }
            if(check()) ans=min(ans,c);
            if (s==0)  break;
        }
        cout << ans << "\n";
    }

}
