#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>
#include<bitset>
#include<cassert>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define FOR3(i,a,b) for(int i=a,i##_end=b;i<i##_end;i++)
#define FOR_EACH(it,v) for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI; 
typedef vector<VI> VVI;
typedef complex<int> xy_t;

template<typename T> void debug(T v , string delimiter = "\n")
{ for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++) cout << *it << delimiter; cout << flush ;}

int dx[]  = {0,1,0,-1};
int dy[]  = {1,0,-1,0};
string ds = "SENW";

const double PI = 4.0*atan(1.0);

int X0[1111];
int Y0[1111];
int X1[1111];
int Y1[1111];

int g[1111][1111];

void addEdge(int from, int to, int cost){
  g[from][to] = g[to][from] = cost;
}

int dist(int p0, int p1, int q0, int q1) {
  int max0 = max(p0, q0);
  int min1 = min(p1, q1);
  return max(0, max0 - min1 - 1);
}

int main() {

  int t,caseNo=1;
  cin>>t;
  while(t--){
    int W,H,B;
    cin>>W>>H>>B;
    FOR(i,B){
      cin>>X0[i]>>Y0[i]>>X1[i]>>Y1[i];
    }
    
    int start = B, goal = B + 1;
    int P = B + 2;
    FOR(i,P) FOR(j,P) g[i][j] = 1<<29;

    FOR(i, B) {
      addEdge(start, i, X0[i]);
      addEdge(i, goal, W-1-X1[i]);
    }
    addEdge(start, goal, W);
    FOR(i, B) FOR(j, i) {
      int d = max(dist(X0[i], X1[i], X0[j], X1[j]), dist(Y0[i], Y1[i], Y0[j], Y1[j]));
      //cout<<"! "<<i<<" "<<j<<" "<<d<<endl;
      addEdge(i, j, d);
    }
    int ans = 0;
    VI label(P, 1<<29);
    VI visited(P);
    label[start] = 0 ;
    visited[start] = true;
    int minidx = start;
    FOR(_, P) {
      FOR(i, P) {
        if(visited[i]) continue;
        if(label[minidx] + g[minidx][i] < label[i]){
          label[i] = label[minidx] + g[minidx][i];
        }
      }

      int mind = 1<<29;
      FOR(i, P) {
        if(visited[i]) continue;
        if(label[i] < mind){
          mind = label[i];
          minidx = i;
        }
      }
      //cout<<"C " << mind<<" "<<minidx<<endl;
      if(minidx == -1) break;
      visited[minidx] = true;
    }
    //FOR(i,P) cout<<" "<<label[i]<<endl;
    ans = label[goal];
    
    printf("Case #%d: %d\n", caseNo++, ans);
    
  }
  return 0 ;
}
