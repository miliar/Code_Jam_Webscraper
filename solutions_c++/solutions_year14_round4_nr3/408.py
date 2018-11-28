#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <numeric>
#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
#define sz(a) ((int)(a).size())
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define Rep(i,j,k) for (int i=(j); i<=(k); i++)
#define Repd(i,j,k) for (int i=(j); i>=(k); i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SUM(a) accumulate(all(a),string())
#define online1
#define RAND ((rand()<<15)+rand())
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#include <cmath>

int W, H, n;
struct Trec{
  int x0, y0, x1, y1;
  void read(){
    cin>>x0>>y0>>x1>>y1;
  }
  void print(){
    cout<<x0<<" "<<y0<<" "<<x1<<" "<<y1<<endl;
  }
} rec[1100];
vector<int>h;

int block[1100][6100];
int dis[1100][6100];
bool inq[1100][6100];
queue<II> Q;

void change(int &x){
  x=find(ALL(h),x)-h.begin();
}

void push(int x0, int y0, int x, int y, int p){
  if (!block[x][y])
    p++;
  if (dis[x][y]==-1 || p<dis[x][y]){
    dis[x][y]=p;
    if (!inq[x][y]){
      inq[x][y]=1;
      Q.push(mk(x,y));
    }
  }
}

int main(){
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);
  int T;
  cin>>T;
  
  Rep(tt,1,T){
    cout<<"Case #"<<tt<<": ";
    cin>>W>>H>>n;
    h.clear();
    h.push_back(0);
    h.push_back(H-1);
    Rep(i,1,n){
      rec[i].read();
      h.push_back(rec[i].y0);
      if (rec[i].y0>0)
      h.push_back(rec[i].y0-1);
      if (rec[i].y0<H-1)
      h.push_back(rec[i].y0+1);
      h.push_back(rec[i].y1);
      if (rec[i].y1>0)
      h.push_back(rec[i].y1-1);
      if (rec[i].y1<H-1)
      h.push_back(rec[i].y1+1);
    }
    sort(ALL(h));
    h.resize(unique(ALL(h))-h.begin());
    //  H=h.size();
    // //cout<<H<<endl;
     Rep(i,1,n){
       //change(rec[i].y0);
         //   // change(rec[i].y1);
    //   // rec[i].print();
     }

    memset(block,0,sizeof block);
    Rep(i,1,n)
      Rep(x,rec[i].x0, rec[i].x1)
      Rep(y,rec[i].y0, rec[i].y1)
      block[x][y]=1;
    memset(dis,0xff,sizeof dis);
    Rep(y,0,H-1)
      push(0,y,0, y, 0);
    while(!Q.empty()){
      int x0=Q.front().fi, y0=Q.front().se;
      Q.pop();
      Rep(dx,-1,1)
        Rep(dy,-1,1) if (dx || dy){
        int x1=x0+dx, y1=y0+dy;
        if (x1<0 || y1<0 || x1>=W || y1>=H)
          continue;
        //cout<<x0<<","<<y0<<"->"<<x1<<","<<y1<<endl;
        push(x0,y0,x1,y1,dis[x0][y0]);
      }
      inq[x0][y0]=0;
    }
    int ans=1<<30;
    // Rep(x,0,W-1){
    //   Rep(y,0,H-1)
    //     cout<<dis[x][y]<<" ";
    //   cout<<endl;
    // }
    Rep(y,0,H-1)
      ans=min(ans, dis[W-1][y]);
    cout<<ans<<endl;
  }

  return 0;
}
