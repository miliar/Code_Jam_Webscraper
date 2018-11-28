#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
inline int toInt(char s) {return s-48;}
template<class T> inline string toStr(T x) {stringstream ss; ss << x;string s; return ss.str();}
inline int powi(int n,int p){ int res=1; for(int i=0;i<p;i++) {res = res*n;} return res; } //no overflow check
template<class T> inline T sqr(T x) {return x*x;}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

bool isPalindrome(int p){
  string str = toStr(p);
  int center = str.size()/2;
  if (center*2 < (int)str.size()) center++;
  bool flag = true;
  for(int q=0; q<center;q++){
    if(str[q] != str[str.size()-1-q]) { flag = false; break;}
  }
  return flag;
}

int main(void){
  ifstream ifs("C-small-attempt0.in");
  string buf;
  getline(ifs,buf);
  int cases = toInt(buf);
  for(int i=0; i<cases; i++){
     getline(ifs,buf);
     stringstream ss(buf);
     int min,max;
     ss >> min;
     ss >> max;
     int mi = sqrt(min);
     if(mi*mi < min) mi++;
     int ma = sqrt(max);
     int num = 0;
     for(int p = mi; p<=ma; p++){
       //cout << p << endl;
       if(isPalindrome(p) && isPalindrome(p*p)) num++;
     }
     cout << "Case #" << i+1 << ": "<< num << endl;
  }
  return 0;
}
