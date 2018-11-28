#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
int g[200][200],c[200],r[200];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Boutput2.txt","w",stdout);

    int T;
    cin>>T;
    for (int cas = 1; cas <=T; cas++){
        memset(c,0,sizeof(c));
        memset(r,0,sizeof(r));
        int n,m;
        cin>>n>>m;
        int i,j;
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++) cin>>g[i][j];
        for (i = 0; i < n; i++){
            for (j = 0; j < m; j++) c[i] = max(c[i], g[i][j]);
            for (j = 0; j < m; j++) r[j] = max(r[j], g[i][j]);
        }
        int flag = 1;
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
                if (g[i][j] < c[i] && g[i][j] < r[j]) {flag = 0; break;}
        cout<<"Case #"<<cas<<": ";
        if (flag) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}

