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


void calc(vector<int>& balls,int main, int k){
  sort(balls.begin(),balls.end());
  //for(int p=0;p<balls.size();p++) cout << balls[p] << " ";
  const int size = balls.size();
  int num = 0;
  if(main==1){
    cout << "Case #" << k << ": " << size << endl;
    return;
  }
  for(int i=0; i<size;i++){
    if(balls[i]>=main){
      int tmp = main; int k=0;
      while(tmp<=balls[i]) {
	tmp = tmp*2-1;k++;
	//cout << tmp;
      }
      if(k<size-i){
	num += k;
	main = tmp;
	main += balls[i];
      }else{
	num += size-i;
	break; //removed all
      }
    }else{
      main += balls[i];
    }
  }
  cout << "Case #" << k << ": " << num << endl;


}

int main(void){
  // vector<int> a(2);
  // a[0]=2;a[1]=1;
  // calc(a,2,1);

  ifstream ifs("A-small-attempt0.in");
  string buf;
  getline(ifs,buf);
  int cases = toInt(buf);
  for(int i=0; i<cases; i++){
     getline(ifs,buf);
     stringstream ss(buf);
     int n,m;
     ss >> n;//main
     ss >> m;//num
     vector<int> X(m);
     getline(ifs,buf);
     stringstream ss2(buf);
     for(int k =0; k<m; k++){
  	 ss2 >> X[k];
     }
     // for(int p=0; p<m;p++){
     //   cout << X[p] << " ";
     // }
     // cout << endl;
     // cout << n << endl;
     calc(X,n,i+1);
  }

  return 0;
}
