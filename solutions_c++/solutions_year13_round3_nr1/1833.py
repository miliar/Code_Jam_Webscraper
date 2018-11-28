#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <numeric>
using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define IREP(it,array) for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it)
#define PREP(it,array) for(vector<P>::iterator it=array.begin(); it!=array.end(); ++it)
#define SREP(it,array) for(vector<string>::iterator it=array.begin(); it!=array.end(); ++it)

#define MP       make_pair
#define PB       push_back
#define ALL(x)   (x).begin(),(x).end()

const int INF = 1<<29;
const double EPS = 1e-9;
double zero(double d){
  return d < EPS ? 0.0 : d;
}

typedef long long LL;
typedef pair<int,int> P;


int main()
{
  cout.setf(ios::fixed, ios::floatfield);
  cout.precision(7);

  int TT;
  cin >> TT;
  REP(targetNum,TT){

    string str;
    int n;
    cin>>str>>n;

    vector<P> satis;
    int s=-1,e=0;
    REP(i,str.size()){
      if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u'){
        s=i;
        e=i;
      }
      else
        e=i;
      
      if(e-s >= n){
        satis.PB(MP(s+1,e));
        s++;
      }
    }
    
    LL res = 0L;
    int prev = 0;
    
    PREP(it,satis){
//      cout << (*it).first << ", " << (*it).second << endl;
      
      int bef = (*it).first - prev+1;
      int aft = str.size() - (*it).second;
      res += bef * aft;

//      cout << "  b: " << bef << "  a: " << aft << endl;

      prev = (*it).first+1;

//      cout << "   p: " << prev << "res: " << res << endl;
      
    }
    

    cout << "Case #" << targetNum+1 << ": " ;
    cout << res;
    cout << endl;
  }
  

  return 0;
}
