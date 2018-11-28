#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

int f[13][5000][5000];
int a[4];
void sortit(int&x,int&y,int&z){
  a[0]=x;a[1]=y;a[2]=z;
  sort(a,a+3);
  x=a[0];y=a[1];z=a[2];
}

bool check(int x,int y,int z,int k) {
  if (x + y + z == 1) return true;
  sortit(x,y,z);
  if(f[k][x][y]!=0)return f[k][x][y]>0;
  // x,y,z>=0 && x+y+z==2^k
  int&ret=f[k][x][y];
  ret=0;
  int a = (x+y-z);
  int b = (z+y-x);
  int c = (x+z-y);
  if(a<0||b<0||c<0||(a&1)||(b&1)||(c&1)){ret=-1;return false;}
  a/=2;b/=2;c/=2;
  x-=a;y-=b;z-=c;
  if(x<0||y<0||z<0){ret=-1;return false;}
  if(check(x,y,z,k-1)){ret=1;return true;}
  ret=-1;return false;
}

int sol[13][3];

int test() {
  int K = 12;
  int N = 1 << K;
  int cnt=0;
  for(int K=1;K<=12;++K){
    N = 1 << K;
  for(int x=0;x<=N;++x){
    for(int y=x;y+x<=N;++y){
      if(N-(x+y)<y) break;
      int z=N-x-y;
      if(check(x,y,z,K)){
        cnt++;
        //cout<<"K = "<<K<<": " << x << " " << y << " "<<z<<endl;
        sol[K][0]=x;
        sol[K][1]=y;
        sol[K][2]=z;
      }
    }
  }
  }
  //cout << cnt << endl;
}

bool okay(int x,int y,int z,int k){
  sortit(x,y,z);
  return sol[k][0]==x&&sol[k][1]==y&&sol[k][2]==z;
}

int win(int a,int b){
  if((a+1)%3==b)return b;
  return a;
}

map<int,string> opt[13][5000];
map<int,int>root[13][5000];

void precalc() {
  opt[1][0][1]="PR";root[1][0][1]=2;
  opt[1][1][0]="PS";root[1][0][1]=0;
  opt[1][1][1]="RS";root[1][0][1]=1;
  for(int K=2;K<=12;++K){
    int N=1<<K;
    for(int x=N/3;x<=N/3+1;++x)
      for(int y=N/3;y<=N/3+1;++y){
        int z = N - x - y;
        if(!okay(x,y,z,K)) continue;
        
        string res="ZZZ";
        int w;
        int M = N >> 1;
        for(int lx=M/3;lx<=M/3+1;++lx){
          for(int ly=M/3;ly<=M/3+1;++ly){
            int lz=M-lx-ly;
            if(!okay(lx,ly,lz,K-1))continue;
            int rx=x-lx;
            int ry=y-ly;
            int rz=z-lz;
            if(!okay(rx,ry,rz,K-1))continue;
            res=min(res,opt[K-1][lx][ly]+opt[K-1][rx][ry]);
          }
        }
        opt[K][x][y]=res;
      }
  }
}

void run() {
  int K,X,Y,Z;
  cin >> K >> Y >> Z >> X;
  int N = 1 << K;
  if(!okay(X,Y,Z,K)){
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << opt[K][X][Y] << endl;
  }
}

int main() {
  //freopen("A.in","r",stdin);
  freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);
  test();
 
  precalc();
  
  int test;
  cin >> test;
  for(int no=1;no<=test;++no){
    cout << "Case #"<<no<<": ";
    run();
  }
}

