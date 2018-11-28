// last update : 2013-04-13 13:27:27 nav

#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;
typedef long long ll;

#define ALL(a)  (a).begin(),(a).end()

const int INF = 1 << 29;
const double EPS = 1e-7;

bool palinrome_number(ll n){
  int keta;
  for(keta = 9; keta > 0; keta--){
    if(n / (ll)pow(10, keta - 1) != 0) break;
  }

  ll u = (ll)pow(10, keta - 1), l = 1;
  while(u >= l){
    ll ud = (n % (u * 10)) / u;
    ll ld = (n % (l * 10)) / l;
    if(ud != ld) return false;
    u /= 10;
    l *= 10;
  }
  return true;
}

int main(int argc, char **argv){
  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    int A, B;
    cin >> A >> B;

    int cnt = 0;
    for(int k = 1; k * k <= B; k++){
      if(A <= k * k){
	if(palinrome_number(k) && palinrome_number(k * k))
	  cnt++;
      }
    }
    cout << "Case #" << i + 1 << ": " << cnt << endl;
  }
}
