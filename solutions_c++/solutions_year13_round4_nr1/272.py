// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

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
#include<cassert>
#include<bitset>

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

struct event
{
  int isAdd;
  long long time;
  long long num;
  event(bool add, long long t,long long n): isAdd(add), time(t), num(n){}

  friend bool operator < (const event& e1, const event& e2)
  {
    if(e1.time != e2.time) return e1.time < e2.time;
    return e1.isAdd > e2.isAdd;
  }
};

int mod =1000002013;

long long cost(long long N,long long distance)
{
  return N * distance - (distance * (distance - 1)) / 2;
}

long long solve()
{
  ll_t N,M;
  cin>>N>>M;
  vector<event> events;
  long long ans = 0, subans = 0;
  FOR(_,M){
    long long o,e,p;
    cin>>o>>e>>p;
    events.push_back(event(true,o,p));
    events.push_back(event(false,e,p));
    ans += cost(N, e-o) % mod * p % mod;
    ans %= mod;
  }
  sort(ALL(events));
#define TIME first
#define NUM second
  multiset<pair<long long,long long> > ms;
  FOR(i,SZ(events)){
    event e = events[i];
    if(e.isAdd){
      ms.insert(MP(e.time, e.num));
      //cout<<"ADD "<<e.time<<" "<<e.num<<endl;
    }else{
      //cout<<"DOWN "<<e.time<<" "<<e.num<<endl;
      while(e.num > 0 && SZ(ms)){
        pair<ll_t, ll_t> last = *ms.rbegin();
        ll_t downNum = min(e.num, last.NUM);
        long long dif = e.time - last.TIME;
        //cout<<" "<<last.TIME<<" "<<e.time<<" "<<downNum<<endl;
        subans += cost(N, dif) % mod * downNum % mod;
        subans %= mod;
        e.num -= downNum;
        last.NUM -= downNum;
        ms.erase(ms.find(*ms.rbegin()));
        if(last.NUM > 0){
          ms.insert(last);
        }
      }
    }
  }
  assert(SZ(ms) == 0);
  return (ans - subans + mod * 10LL) % mod;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    ll_t ans = solve() ;
    printf("Case #%d: %lld\n" , case_no++ , ans);
    
  }
  return 0 ;
}
