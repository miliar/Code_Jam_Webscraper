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


inline int isfilled(vector<int> X,int pos, int val){
  if(X[pos]==0 || X[pos]==val) return 1;
  else return 0;
}

#define IS(y) isfilled(X,y,X[pos])

int isline(vector<int>& X, int pos,int m, int n){
  int q = pos / m;
  int p = pos % m;
  int isgood = 0;
  int tmp=1;
  for(int i=0; i<m; i++){
    tmp *= IS(q*m+i);
  }
  if(tmp==1){
    isgood =1;
    for(int i=0; i<m; i++){
      X[q*m+i] = 0;
    }
  }
  tmp = 1;
  for(int i=0; i<n; i++){
    tmp *= IS(i*m+p);
  }
  if(tmp==1){
    isgood =1;
    for(int i=0; i<n; i++){
      X[i*m+p] = 0;
    }
  }

  // for(int i=0; i<n;i++){
  //   for(int j=0; j<m;j++){
  //     cout << X[m*i+j] << " ";
  //   }
  //   cout << endl;
  // }

  return isgood;
}


int main(void){
  ifstream ifs("B-large.in");
  string buf;
  getline(ifs,buf);
  int cases = toInt(buf);
  for(int i=0; i<cases; i++){
     getline(ifs,buf);
     stringstream ss(buf);
     int n,m;
     ss >> n;
     ss >> m;
     vector<int> X(n*m,-1);
     multimap<int,int> num;
     set<int> kind;
     for(int j=0; j<n; j++){
       getline(ifs,buf);
       stringstream ss2(buf);
       for(int k =0; k<m; k++){
	 ss2 >> X[j*m+k];
	 num.insert(pair<int,int>(X[j*m+k],j*m+k));
	 kind.insert(X[j*m+k]);
       }
     }
     
     // for (int p=0;p<n;p++){
     //   for (int q=0;q<m;q++){
     // 	 cout << X[p*m+q] << " ";
     //   }
     //   cout << endl;
     // }
     int flag = 0;
     set<int>::iterator it = kind.begin();
     while(it != kind.end()){
       //cout << *it <<endl;
       multimap<int,int>::iterator it2 = num.lower_bound(*it);
       while(it2 != num.upper_bound(*it)){
	 //cout << "   " << (*it2).second << endl;
	 if(isline(X,(*it2).second,m,n)==0) { flag =1;break;}
	 it2++;
       }
       if(flag==1) break;
       it++;
     }
     cout << "Case #" << i+1;
     if(flag==1) cout << ": NO" << endl;
     else cout << ": YES" << endl;

  }


  return 0;
}
