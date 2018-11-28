#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int n,m,t,a[101][101]={0},h[101]={0},l[101]={0};
int maxh[101]={0},maxl[101]={0};
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    cin>>t;int f;
    for(int k=1;k<=t;++k)
    {
        memset(a,0,sizeof(a));
        memset(h,0,sizeof(h));
        memset(l,0,sizeof(l));
        memset(maxh,0,sizeof(maxh));
        memset(maxl,0,sizeof(maxl));
        cin>>n>>m;f=1;
        for(int i=1;i<=n;++i)
            for(int j=1;j<=m;++j)
            {
                cin>>a[i][j];
                if(a[i][j]>maxh[i]) maxh[i]=a[i][j];
                if(a[i][j]>maxl[j]) maxl[j]=a[i][j];
            }
        for(int i=1;i<=n&&f;++i)
        {
            for(int j=1;j<=m&&f;++j)
            {
                if(a[i][j]<maxh[i])
                {
                    if(l[j]==0) l[j]=a[i][j];
                    else if(a[i][j]!=l[j]) {f=0;break;}
                }
            }
        }
        for(int i=1;i<=m;i++) if(l[i]<maxl[i]&&l[i]) f=0;
        cout<<"Case #"<<k<<": ";
        if(f) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
