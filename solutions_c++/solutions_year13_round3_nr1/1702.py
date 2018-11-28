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

bool a[101];
int N;
bool chaeck(int S, int E){

   for(int i=S; i<E-N+1; i++){
      int cnt = 0;
      for(int j=0; j<N; j++){
         if(a[i+j]) cnt++;
         else cnt = 0;
         if(cnt == N)return true;
      }
   }
   return false;
}

int main(){
   int n;
   cin >> n;
   for(int t=1; t<=n; t++){
      int ans = 0;
      string s;
      cin >> s >> N;
      for(int i=0; i<s.size(); i++){
         if(s[i] == 'a' || s[i] == 'i' || s[i] == 'u' || s[i] == 'e' || s[i] == 'o') a[i] = 0;
         else a[i] = 1;
      }
      for(int i=0; i<=s.size()-N; i++){
         for(int j=i+N; j<=s.size(); j++){
            if(chaeck(i,j))ans++;
//            cout << "i = " << i << "j = " << j << endl;
         }
      }

      cout << "Case #" << t << ": " << ans << endl;
   }
  return 0;
}
