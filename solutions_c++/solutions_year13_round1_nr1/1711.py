#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define D(x) cerr << #x << " = " << x << endl
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define FOREACH(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define ALL(v) (v).begin(), (v).end()


typedef long long int64;

const int INF = (int)(1e9);
const int64 INFLL = (int64)(1e18);
const double EPS = 1e-13;
const double PI = acos(-1.0);

using namespace std;

string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

int main() {
  ios_base::sync_with_stdio(false);
  freopen("a-small.in","r",stdin);
  freopen("a-small.out","w",stdout);
  int64 c;
  cin >> c;
  for(int k=1; k<=c;k++){
    int64 r,t;
    cin >> r >> t;
    int64 ans = 0;
    int64 area = 0;
    r++;
    while(true){
      area = (r*r) - ((r-1)*(r-1));
      
      if(t >= area){
        ans++;
        t -= area;
      }else
        break; 
      r+=2;
      
        
    }
    cout <<"Case #"<<k<<": "<<ans<< endl;
    
    
  }
  return 0;
}

