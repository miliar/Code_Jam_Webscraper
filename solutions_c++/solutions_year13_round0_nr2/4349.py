#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define EREP(i,a,b) for(int i=a;i<=b;i++)
#define erep(i,n) EREP(i,0,n)
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

/*
必ず高さが高い芝から処理していく必要がある。
低い芝を先に処理すると、高い芝がその低い芝に合わせて高さが変わってしまうことがあるから。

入力の中に含まれる高さで順番にカットしていく(100種)。
- 普通に100から順番に1ずつ下げて試していっても大丈夫

ある高さhの芝刈り機で処理するとき。
- x方向にhでカットできる場所があるならカットする
- y方向にhでカットできる場所があるならカットする

カットできる条件
- 高さhの芝刈り機で、直線状にカットしようとしたとき
- この直線上にhより高い芝があってはいけない。

計算量 O(100(芝の高さ種類数) * 100(W) * 100(H))
 */

int h, w;
int input[102][102];
int t[102][102];

void cut(int a, int sx, int sy, int dx, int dy){
  int x = sx;
  int y = sy;

  while(input[y][x] != -1){
    if(input[y][x] > a) return ;
    x += dx;
    y += dy;
  }

  x = sx;
  y = sy;

  while(input[y][x] != -1){
    if(a < t[y][x]) t[y][x] = a;
    x += dx;
    y += dy;
  }
}

bool solve(){
  for(int i = 0; i < h; i++){
    for(int j = 0; j < w; j++){
      t[i][j] = 100;
    }
  }

  for(int a = 99; a >= 1; a--){
    //x方向にカット
    for(int i = 0; i < h; i++){
      cut(a, 0, i, 1, 0);
    }

    //y方向にカット
    for(int i = 0; i < w; i++){
      cut(a, i, 0, 0, 1);
    }
  }

  for(int i = 0; i < h; i++){
    for(int j = 0; j < w; j++){
      if(input[i][j] != t[i][j]) return false;

      //cout << t[i][j] << " ";
    }
    //cout << endl;
  }
  return true;
}

int main(void){
  int T;
  cin >> T;

  for(int CASE = 1; CASE <= T; CASE++){
    memset(input, -1, sizeof(input));

    cout << "Case #" << CASE << ": ";
    cin >> h >> w;
    for(int i = 0; i < h; i++){
      for(int j = 0; j < w; j++){
        cin >> input[i][j];
      }
    }
    cout << (solve() ? "YES" : "NO") << endl; 
  }
}
