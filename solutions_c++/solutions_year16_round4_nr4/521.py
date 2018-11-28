#include<bits/stdc++.h>
using namespace std;

#define sin(x) scanf("%d",&x)
#define sin2(x,y) scanf("%d%d",&x,&y)
#define sin3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define pb push_back
#define mp make_pair
#define y1 asdnqw
#define next mdamdamda
#define right praviy
#define x first
#define y second
const int N=2e5+5;
const double eps=0.1;
#define double long double
int cost,a[8][8],u[8],n,b[8][8];
int wex[8];
bool well;
int ans;
int ff;
void f(int r){
    if(r>n)return;
    bool ok=0;
    for(int i=1;i<=n;++i)
    if(a[wex[r-1]][i]&&!u[i]){
        u[i]=1;
        f(r+1);
        u[i]=0;
        ok=1;
    }
    if(!ok)well=0;
}
void check(){
    well=1;
    for(int i=0;i<n;++i)
        wex[i]=i+1;
    do{
        f(1);
        if(ff==63){
              //  for(int i=0;i<n;++i)
               // cout<<wex[i]<<' ';
              //  cout<<endl;
        }

    }while(next_permutation(wex,wex+n));
    if(well&&ans>cost){
        ans=cost;
        for(int i=1;i<=n;++i)
            for(int j=1;j<=n;++j)
                b[i][j]=a[i][j];

    }
}
void go(int x,int y){
    if(cost>ans)return;
    if(x>n){
        ++ff;
        check();
        return;
    }
    if(y>n){
        y=1;
        go(x+1,y);
        return;
    }
    if(a[x][y]==1){
        go(x,y+1);
        return;
    }
    a[x][y]=1;
    ++cost;
    go(x,y+1);
    a[x][y]=0;
    --cost;
    go(x,y+1);
}
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    int kl=0;
    cin>>test;
    for(;test;--test){
    ++kl; cout<<"Case #"<<kl<<": ";
    cin>>n;
    char ch;
    for(int i=1;i<=n;++i)
        for(int j=1;j<=n;++j)
            cin>>ch,a[i][j]=ch-'0';
    ans=1e9;
    go(1,1);
    cout<<ans<<'\n';
    //for(int i=1;i<=n;++i){cout<<'\n';for(int j=1;j<=n;++j)cout<<b[i][j];}cout<<'\n';

  }
}
