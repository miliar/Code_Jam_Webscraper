#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;
const int inf = 100000000;

const int MaxR = 1000;
vector<int> X,Y;
int W, H, N;

struct Rect {
  int x1, x2, y1, y2;
  int read() {
    scanf("%d %d %d %", &x1, &y1, &x2, &y2);
    X.push_back(x1); Y.push_back(y1);
    X.push_back(x2); Y.push_back(y2);
  }
}R[MaxR];

int A[MaxR][MaxR];

int D[MaxR][MaxR];

int check(int &a,int b)
{
  if(a < 0 || b < a) {a=b; return true;}
  return false;
}

struct data {
  int x,y,d;
  inline int set(int _x,int _y,int _d){
    x=_x;y=_y;d=_d;
  }
}dat;
bool operator < (const data&a, const data&b){
  return a.d > b.d; 
}

int run() {
  scanf("%d %d %d", &W, &H, &N);
  for(int i=0;i<W;++i)
    for(int j=0;j<H;++j)
      A[i][j]=0,D[i][j] = -1;
  for(int i=0;i<N;++i) {
    int x1, y1, x2, y2;
    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    for(int x =x1;x<=x2;++x)
      for(int y=y1;y<=y2;++y)
        A[x][y] = 1;
  }
  priority_queue<data> Q;
  for(int h=0;h<H;++h){
    D[0][h] = 1 - A[0][h];
    dat.set(0,h,D[0][h]);
    Q.push(dat);
  }
  int ans = W;
  while(!Q.empty()) {
    data tmp = Q.top(); Q.pop();
    int x = tmp.x, y = tmp.y, cur = tmp.d;
    if(cur != D[x][y]) continue;
    if(x == W - 1) {
      ans = cur;
      break;
    }
    for(int dx = -1; dx <= 1; ++ dx)
      for(int dy = -1; dy <= 1; ++ dy) {
        int xx = x + dx;
        int yy = y + dy;
        if(xx<0||xx>=W||yy<0||yy>=H) continue;
        if(dx == 0 && dy == 0) continue;
        int td = cur + 1 - A[xx][yy];
        if(check(D[xx][yy], td)) {
          dat.set(xx,yy,td);
          Q.push(dat);
        }
      }
  }
  return ans;
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	int test;scanf("%d",&test);
	for(int no=1;no<=test;++no)
	 printf("Case #%d: %d\n", no, run());
}
