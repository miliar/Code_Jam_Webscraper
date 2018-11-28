#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXN 105
using namespace std;
int n,m;
int mat[MAXN][MAXN];
bool exist[MAXN],vist[MAXN][MAXN];
bool valide(int val){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            bool t1=true,t2=true;
            if(mat[i][j]==val){
                for(int k=1;k<=m;k++)
                 if(mat[i][k]>val) t1=false;
                for(int k=1;k<=n;k++)
                 if(mat[k][j]>val) t2=false;
                if(!t1&&!t2) return false;
            }
        }
    }
    return true;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int test,t=1;
    cin>>test;
    while(t<=test){
        cin>>n>>m;
        memset(exist,false,sizeof(exist));
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                cin>>mat[i][j];
                exist[mat[i][j]]=true;
            }
        }
        bool tag=true;
        for(int i=1;i<=100;i++){
            if(exist[i]){
                if(!valide(i)) tag=false;
                break;
            }
        }
        if(tag) cout<<"Case #"<<t++<<": YES"<<endl;
        else  cout<<"Case #"<<t++<<": NO"<<endl;
    }


    return 0;
}
