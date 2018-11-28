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

int main(){
   int T;
   cin >> T;
   for(int t=1; t<=T; t++){
      int field[101][101];
      int lawn[101][101];
      fill(lawn[0],lawn[101],-1);
      int N,M;
      bool flag = true;
      cin >> N >> M;
      int Max = 0;
      for(int i=0; i<N; i++){
         for(int j=0; j<M; j++){
            cin >> field[i][j];
            Max = max(Max,field[i][j]);
         }
      }

      for(int i=0; i<N; i++){
         for(int j=0; j<M; j++){
            if(field[i][j] == Max) lawn[i][j] = Max;
         }
      }
      

      for(int j=0; j<M; j++){
         if(field[0][j] == Max)continue;
         bool f = true;
         for(int i=0; i<N; i++){
            if(field[i][j] == Max){
               f = false;
               break;
            }
         }

         if(f){
            for(int i=0; i<N; i++){
               lawn[i][j] = Max;
            }
         }
      }


      for(int i=0; i<N; i++){
         if(field[i][0] == Max)continue;
         bool f = true;
         for(int j=0; j<M; j++){
            if(field[i][j] == Max){
               f = false;
               break;
            }
         }
         
         if(f){
            for(int j=0; j<M; j++){
               lawn[i][j] = Max;
            }
         }
      }
      

      int a = Max;
      for(int i=0; i<N; i++){
         for(int j=0; j<M; j++){
            if(lawn[i][j] != a){
               flag = false;
            }
         }
      }

      /*   for(int i=0; i<N; i++){
         for(int j=0; j<M; j++){
            cout << lawn[i][j];
         }
         cout << endl;
         }*/
      
      cout << "Case #" << t << ": ";
      if(flag) cout << "YES" << endl;
      else cout << "NO" << endl;
   }
  return 0;
}
