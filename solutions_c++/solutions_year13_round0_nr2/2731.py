#include <iostream>
#include <cstdio>
using namespace std;
#define N 17
#define M 17
int cse;
int inp[N][M];
int myinp[N][M];
int n,m;

void chk(int x,int y,int dx,int dy){
    int i=x;
    int j=y;
    bool flg=0;
    for(;i>=0&&i<n&&j>=0&&j<m;i=i+dx,j=j+dy){
        if(inp[i][j]==2) flg=1;
    }
    if(flg)return;

    //cout<<x<<y<<dx<<dy<<endl;
    i=x;j=y;
    for(;i>=0&&i<n&&j>=0&&j<m;i=i+dx,j=j+dy) myinp[i][j]=1;
}


int main(){
    freopen("b.txt","rt",stdin);
    freopen("b.out","wt",stdout);
    cin>>cse;
   for(int run=1;run<=cse;run++){
        cin>>n>>m;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++){
                cin>>inp[i][j];
                //cout<<inp[i][j];
                myinp[i][j]=2;
            }

        for(int i=0;i<n;i++) chk(i,0,0,1);
        for(int j=0;j<m;j++) chk(0,j,1,0);
        bool flg=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(myinp[i][j]!=inp[i][j]) flg=1;

        cout<<"Case #"<<run;
        if(flg) cout<<": NO\n";
        else cout<<": YES\n";

    }
    return 0;
}
