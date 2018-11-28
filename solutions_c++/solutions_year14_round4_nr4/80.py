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

int mod = 1000000007;

struct result {
  ll_t value;
  ll_t pattern;
};

vector<string> S;

int group[111];
int first[111];

int prefixesNum(int N) {
  int p = 0 ;
  FOR(t,N){
    set<string> s;
    FOR(i,SZ(S)){
      if(group[i] == t){
        FOR(j,SZ(S[i])) {
          s.insert(S[i].substr(0, j+1));
        }
      }
    }
    p += SZ(s) + 1;
  }
  return p;
}

bool check(int N){ // group
  FOR(i,N) if(first[i] == -1) return false; // none group
  //FOR(i,N-1) if(first[i] > first[i+1]) return false;
  return true;
}

result dfs(int M, int N, int pos = 0){
  if(pos == SZ(S)){
    FOR(i,N) first[i] = -1;
    FOR(i,SZ(S)) {
      if(first[group[i]] == -1) first[group[i]] = i;
    }
    if(!check(N)) return (result){0, 0};
    //FOR(i,M) cout<<" "<<group[i]; cout<<endl;
    result sub;
    sub.value = prefixesNum(N);
    sub.pattern = 1;
    return sub;
  }
  result ans ;
  ans.value = -1;
  FOR(i,N) {
    group[pos] = i;
    result sub = dfs(M, N, pos + 1);
    if(ans.value < sub.value) {
      ans.value = sub.value;
      ans.pattern = sub.pattern;
    }else if(ans.value == sub.value) {
      ans.pattern += sub.pattern;
      ans.pattern %= mod;
    }
  }
  return ans;
}

int main() {

  int t,caseNo=1;
  cin>>t;
  while(t--){
    int M,N;
    cin>>M>>N;
    S.resize(M);
    FOR(i,M) cin>>S[i];
    result res = dfs(M, N, 0);
    printf("Case #%d: %d %d\n", caseNo++, (int)res.value, (int)res.pattern);
    
  }
  return 0 ;
}
