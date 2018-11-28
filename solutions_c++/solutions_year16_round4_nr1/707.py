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
int a[N],qq[N],n,q,w,e,sz;
int f(int v,int h,int col){
    a[v]=col;
    if(h<=n){
        if(col==0){
            f(v*2,h+1,0);
            f(v*2+1,h+1,1);
        }
        if(col==1){
            f(v*2,h+1,1);
            f(v*2+1,h+1,2);
        }
        if(col==2){
            f(v*2,h+1,2);
            f(v*2+1,h+1,0);
        }
    }
}
string s;
vector<string> vot;
string g(int v,int h){
    if(h>n){
        if(a[v]==0)return "P";
        if(a[v]==1)return "R";
        if(a[v]==2)return "S";
    }
    string q,w;
    q=g(v*2,h+1);
    w=g(v*2+1,h+1);
    if(q>w)swap(q,w);
    return q+w;
}
void vev(){
    s=g(1,1);
    vot.pb(s);
}
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    int kl=0;
    cin>>test;
    for(;test;--test){
        vot.clear();
            ++kl;
    cout<<"Case #"<<kl<<": ";
    cin>>n>>w>>q>>e;
    sz=1;
    for(int i=1;i<=n;++i)
        sz*=2;
    bool ok=0;
    for(int z=0;z<3;++z){
    qq[0]=qq[1]=qq[2]=0;
    f(1,1,z);
    for(int i=0;i<sz;++i)
        ++qq[a[i+sz]];
    if(qq[0]==q&&qq[1]==w&&qq[2]==e){
        vev();
        ok=1;
    }
    }
    if(!ok){
        cout<<"IMPOSSIBLE\n";
    }else {
        sort(vot.begin(),vot.end());
        cout<<vot[0]<<'\n';
    }
  }
}
