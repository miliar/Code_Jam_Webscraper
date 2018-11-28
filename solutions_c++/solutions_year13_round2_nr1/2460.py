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

ll A,N;
ll a[1000001];
ll memo[10000];
int ans,cnt;

int dfs(int value, int add, int del, int n, int pos){
//   cout <<"value = " << value << "add = " << add << " del = " << del << endl;
//   cout << "n = " << n << "pos = " << pos << endl;
   
   if(memo[value] != -1) return memo[value];

   int res = N;
   
   if(n >= N){
      res = min(res,add-cnt+del);
   }
   
   else {
      for(int i=pos; i<N-del; i++){
         bool flag = false;
         int now = i;
         while(value > a[i] && i<N-del) value += a[i++],flag = true;

         if(i == N-del){
            return memo[value] = add-cnt+del;
         }
         
         res = min(res,min(dfs(value,add,del+1,n+1,pos+i-now),
                           dfs(value+(value-1),add+1,del,n+1,pos+i-now)));
         
         if(flag)i--;
      }
   }

   return memo[value] = res;
}
int main(){
   int T;
   cin >> T;
   for(int t=1; t<=T; t++){

      cin >> A >> N;

      for(int i=0; i<N; i++) cin >> a[i];
      sort(a,a+N);
      ans = N;
      int n = N;
      cnt = 0;
      memset(memo,-1,sizeof(memo));
      for(int i=0; i<n; i++){
         if(A > a[i]) A += a[i],cnt++;
      }

      if(A == 1) ans = n;
      else ans = dfs(A,cnt,0,cnt,cnt);
      cout << "Case #" << t << ": " << ans << endl;
      
   }
  return 0;
}
