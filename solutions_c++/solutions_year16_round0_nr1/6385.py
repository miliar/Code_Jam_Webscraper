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

int T;
LL N;
map<int, bool> M;

void init(){
  M.clear();
}

LL solve(){

  LL ret = 0;
  while(M.size() < 10){
    
    ret += N;

    stringstream ss;
    ss << ret;
    string s = ss.str();

    for(int i = 0; i < s.length(); i++){
      M[s[i] - '0'] = true;
    }

  }

  return ret;

}

int main(){

  cin >> T;

  for(int testCase = 0; testCase < T; testCase++){
    cin >> N;
    init();
    if(N == 0)
      printf("Case #%d: INSOMNIA\n", testCase+1);
    else{
      printf("Case #%d: %lld\n", testCase+1, solve());
    }
  }  

  return 0;

}
