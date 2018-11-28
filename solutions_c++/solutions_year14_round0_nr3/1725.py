#include <iostream>
#include <iomanip>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)

int m,n,k;
int a[10],b[10];
bool xong;
char c[10][10];

void thu(int i){
  if(xong)return;
  if(i==m){
    bool have=false, bad=false;
    Rep(u,m)if(a[u]<b[u]){
      if(have && u>0 && a[u-1]==b[u-1]) bad=true;
      have=true;
    }
    Rep(u,m-1)if(a[u]<b[u]&&a[u+1]<b[u+1]){
      if(max(a[u],a[u+1])>=min(b[u],b[u+1]))bad=true;
    }
    if(!bad){
      int total=0;
#define up(z) x=min(x,max(a[z]-1,0)),y=max(y,min(b[z]+1,n))
      Rep(u,m){
        int x=111,y=-1;
        if(a[u]<b[u])up(u);
        if(u>0&&a[u-1]<b[u-1])up(u-1);
        if(u+1<m&&a[u+1]<b[u+1])up(u+1);
        if(x<y)total+=y-x;
      }
      if(total==m*n-k){
        xong=true;
        bool coc=false;
        Rep(u,m){
          int x=111,y=-1;
          if(a[u]<b[u])up(u);
          if(u>0&&a[u-1]<b[u-1])up(u-1);
          if(u+1<m&&a[u+1]<b[u+1])up(u+1);
          if(x<y){
            for(int v=x;v<y;++v)c[u][v]='.';
          }
          if (a[u]<b[u]&&!coc){
            coc=true;
            c[u][a[u]]='c';
          }
        }
      }
    }
    return;
  }
  for(a[i]=0;a[i]<n;++a[i])for(b[i]=a[i];b[i]<=n;++b[i]){
    thu(i+1);
  }
}

int main() {
  int ntest;
  cin >> ntest;
  Rep(t,ntest){
    cout<<"Case #"<<t+1<<":"<<endl;
    cin>>m>>n>>k;
    xong=false;
    memset(c,0,sizeof(c));
    Rep(i,m)Rep(j,n)c[i][j]='*';
    if(k==m*n-1)c[0][0]='c',xong=true; else thu(0);
    if(xong){
      Rep(i,m){Rep(j,n)cout<<c[i][j];cout<<endl;}
    } else cout<<"Impossible\n";
  }
  return 0;
}
