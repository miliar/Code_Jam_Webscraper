#include <bits/stdc++.h>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.0002
using namespace std;
const int N=202;
int n,m;
char c[N][N];
int a[N][N];

void input(){
    cin>>n>>m;
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++) cin>>c[i][j];
}

int sol(){
    int s,ans=0;
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++)
    a[i][j]=a[i-1][j]+a[i][j-1]-a[i-1][j-1]+(c[i][j]!='.');

    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++)
    if (c[i][j]!='.'){

        if (c[i][j]=='^') s=a[i][j]-a[i][j-1];
        if (c[i][j]=='v') s=a[n][j]-a[n][j-1]-a[i-1][j]+a[i-1][j-1];
        if (c[i][j]=='>') s=a[i][m]-a[i][j-1]-a[i-1][m]+a[i-1][j-1];
        if (c[i][j]=='<') s=a[i][j]-a[i-1][j];
        if (s==1)
        {
            ans++;
            if (a[i][m]-a[i-1][m]+a[n][j]-a[n][j-1]==2) return -1;
        }

    }
    return ans;
}

int main() {
    freopen("A2.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int testn=1;
    cin>>testn;
    for (int test=1;test<=testn;test++){
        input();
        int ans=sol();
        if (ans!=-1)cout<<"Case #"<<test<<": "<<ans<<endl; else
                    cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
    }

    return 0;
}
