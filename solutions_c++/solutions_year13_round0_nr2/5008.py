#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int ncase=1,t,n,m,i,j;
    int a[15][15];
    cin>>t;
    while(t--){
        cin>>n>>m;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                cin>>a[i][j];
            }
        }

        int flag=0;

        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                if(a[i][j]==1){
                    int flag1=0,flag2=0;
                    for(int ii=1;ii<=n;ii++){
                        if(a[ii][j]!=1)
                           flag1=1;
                    }

                    for(int ii=1;ii<=m;ii++){
                        if(a[i][ii]!=1)
                          flag2=1;
                    }

                    if(flag1&&flag2)
                       flag=1;
                }
            }

        }
        cout<<"Case #"<<ncase++<<": ";
            if(flag)
                cout<<"NO"<<endl;
            else
                cout<<"YES"<<endl;
    }
    return 0;
}
