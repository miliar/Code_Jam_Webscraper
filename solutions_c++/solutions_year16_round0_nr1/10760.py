#include <algorithm>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz size()
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) (c).begin(), (c).end()
#define rep(i,a,b) for(int i=(a);i<(b);++i)
#define clr(a, b) memset((a), (b) ,sizeof(a))

#define MOD 1000000007

int main(){
  int t;
  cin>>t;
  rep(i,0,t){
    int n;
    cin>>n;
    int d[10];
    clr(d,0);
    int ans = 0;
    int flag1 = 0;
    rep(j,1,100){
      int a = n*j;
      for(int k = a; k > 0; k/=10){
        d[k%10]++;
      }
      int flag = 1;
      rep(i,0,10){
        if(d[i]==0)flag = 0;
      }
      if(flag == 1){
        ans = a;
        flag1 = 1;
        break;
      }
    }
    if(flag1==0){
      cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
    }
    else{
      cout << "Case #" << i+1 << ": " << ans << endl;
    }
  }
  return 0;
}


