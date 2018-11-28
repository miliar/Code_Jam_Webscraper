#include <bits/stdc++.h>
#define For(i,l,r) for (int r_=(r),i=(l);i<=r_;i++)
#define Rep(i,n) for (int i=0,n_=(n);i<n;i++);
using namespace std;
const int mN=120;
char a[mN][mN];
int n,m;
const int ux[]={0,0,1,0,-1},
          uy[]={0,1,0,-1,0};
int isar(char c)
{
    if (c=='>')
        return 1;
    if (c=='v')
        return 2;
    if (c=='<')
        return 3;
    if (c=='^')
        return 4;
    return 0;
}
bool exar(int f,int i,int j)
{
    while (i>=1 && i<=n && j>=1 && j<=m)
    {
        i+=ux[f];
        j+=uy[f];
        if (i>=1 && i<=n && j>=1 && j<=m)
            if (isar(a[i][j]))
                return true;
    }
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ta;
    cin>>ta;
    For(tz,1,ta)
    {
        printf("Case #%d: ",tz);
        cin>>n>>m;
        For(i,1,n)
            For(j,1,m)
            {
                char c;
                do
                {
                    cin>>c;
                }
                while (isspace(c));
                a[i][j]=c;
            }
        int k;
        int can=true;
        int ans=0;
        For(i,1,n)
            For(j,1,m)
                if (k=isar(a[i][j]))
                {
                    if (exar(k,i,j))
                        continue;
                    else
                    {
                        ans++;
                        bool flag=false;
                        For(v,1,4)
                            if (exar(v,i,j))
                            {
                                flag=true;
                                break;
                            }
                        if (!flag)
                            can=false;
                    }
                }
        if (can)
            cout<<ans<<endl;
        else
            puts("IMPOSSIBLE");
    }
}
