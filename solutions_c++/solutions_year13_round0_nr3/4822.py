#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <set>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <stack>
#include <sstream>
#include <climits>
#include <queue>
#include <cctype>

#define mp make_pair

#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define REP(i,s,n) for(int i=(s); i<(int)(n); i++)
#define ALL(c) (c).begin(),(c).end()

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};
//int dx[] = {0,1,1,1,0,-1,-1,-1};
//int dy[] = {1,1,0,-1,-1,-1,0,1};
const int MAX = 101;
const int INF = 1<<29;

using namespace std;

typedef long long ll;
typedef pair<int,int> P;

vector<ll>v;

string toStr(ll a){
   ostringstream oss;
   oss << a;
   return oss.str();
}

bool isPalin(ll a){
   string s = toStr(a);
   string s2 = s;
   reverse(s2.begin(),s2.end());
   return s == s2;
}

void init(){
   for(ll i=1; i*i<=1000; i++){
      if(isPalin(i*i) && isPalin(i))v.push_back(i*i);
   }
}
int main(){
   init();
   // for(int i=0; i<v.size(); i++)
   //    cout << v[i] << endl;
   int T;
   cin >> T;
   for(int t=1; t<=T; t++){
      ll A,B;
      int cnt = 0;
      cin >> A >> B;
      for(int i=A; i<=B; i++){
         if(binary_search(v.begin(),v.end(),i)) cnt++;
      }
      cout << "Case #" << t << ": ";
      cout << cnt << endl;
   }
  return 0;
}
