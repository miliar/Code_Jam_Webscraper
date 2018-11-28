#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <queue>
#include <complex>
  
#define INF 100000000
#define YJ 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define INF_LL 9223372036854775
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long
#define LD long double 

using namespace std;

#define MAX_N 105

int T;
string str;

int dp[MAX_N][2]; //+-

void init(){
  for(int i = 0; i < MAX_N; i++){
    for(int j = 0; j < 2; j++){
      dp[i][j] = INF;
    }
  }
}

int solve(){

  init();

  dp[0][0] = dp[0][1] = 0;

  for(int i = 0; i < str.length(); i++){
    if(str[i] == '+'){
      dp[i+1][0] = min(min(dp[i+1][0], dp[i][0]),
		       dp[i][1] + 1);
      dp[i+1][1] = min(dp[i+1][1], 
		       min(dp[i+1][0]+1, dp[i+1][1] + 2));
    }
    else{
      dp[i+1][1] = min(min(dp[i+1][1], dp[i][1]),
		       dp[i][0] + 1);
      dp[i+1][0] = min(dp[i+1][0], 
		       min(dp[i+1][0] + 2, dp[i+1][1] + 1));
    }
  }

  return dp[str.length()][0];

}

int main(){

  cin >> T;

  for(int testCase = 0; testCase < T; testCase++){
    cin >> str;
    printf("Case #%d: %d\n", testCase+1, solve());
  }  

  return 0;

}
