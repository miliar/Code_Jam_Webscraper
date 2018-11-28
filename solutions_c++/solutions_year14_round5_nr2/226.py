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

int H[222];
int G[222];

ll_t memo[222][5001][2];

long long DivUpper(long long x, long long y) {
  if (y < 0) return DivUpper(-x, -y);
  if (x <= 0) return x / y;
  return x / y + (x % y == 0 ? 0 : 1);
}

int P,Q,N;

ll_t dfs(int pos, int skipNum, int turn){
  assert(skipNum < 5000);
  if(skipNum > 5000) skipNum = 5000;
  if(pos == N) return 0 ;
  ll_t& ret = memo[pos][skipNum][turn];
  if(ret != -1) return ret;
  ll_t val = 0 ;
  //cout<<pos<<" "<<skipNum<<" "<<turn<<endl;
  // give up
  {
    int hp = H[pos];
    if(turn == 1) hp -= Q;
    int skip = 0;
    while(hp > 0){
      hp -= Q;
      skip++;
    }
    val = dfs(pos + 1, skipNum + skip, 0);
  }
  {
    for(int useSkip=0;useSkip <= skipNum; useSkip++) {
      int hp = H[pos];
      hp -= useSkip * P;
      if(hp <= 0) {
        val = max(val, dfs(pos+1, skipNum-useSkip, turn) + G[pos]);
        continue;
      }
      if(turn) hp -= Q;
      if(hp <= 0) continue;
      bool ok = false;
      while(hp > 0){
        if(Q <= P || (hp % Q > 0 && hp % Q <= P)) { // no need to attack
          ok = true;
          break; 
        }
        hp -= P;
        hp -= Q;
      }
    //cout<<useSkip<<" "<<hp<<" "<<ok<<endl;
      if(!ok) continue;
      int addSkip = 0;
      while(hp - Q > 0) {
        addSkip++;
        hp -= Q;
      }
      //cout<<pos<<" "<<skipNum<<" "<<turn<<" "<<useSkip<<" "<<hp<<endl;
      assert(hp > 0 && hp <= P);
      val = max(val, dfs(pos+1, skipNum-useSkip+addSkip, 1) + G[pos]);
    }
  }
  return ret = val;
}

int main() {
  int t,caseNo=1;
  cin>>t;
  while(t--){
    cin>>P>>Q>>N;
    FOR(i,N) scanf("%d%d",&H[i], &G[i]);
    memset(memo , -1 , sizeof(memo));
    printf("Case #%d: %lld\n", caseNo++, dfs(0, 0, 0));
    
  }
  return 0 ;
}
