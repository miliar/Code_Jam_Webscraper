#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int main() {
  int t;
  cin >> t;
  REP(rep,t){
    int n,x;
    cin >> n >> x;
    int hoge;
    vector<int> s;
    vector<int> used;
    REP(i,n){
      cin >> hoge;
      s.push_back(hoge);
      used.push_back(0);
    }
    int sum = 0;
    int ls = 0;
    sort(s.begin(),s.end());
    for(int i=n-1;i>=0;i--){
      if(ls>i)break;
      if(s[i]+s[ls]<=x){
	sum+=1;
	ls++;
      }else{
	sum += 1;
      }
    }
    cout << "Case #"<<rep+1 << ": "<<sum << endl;
  }


  
  return 0;
}
