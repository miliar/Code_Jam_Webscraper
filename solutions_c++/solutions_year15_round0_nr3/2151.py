#include <bits/stdc++.h>
using namespace std;

typedef complex<int> int_c;
typedef vector<int_c> quaternion;
typedef long long ll;

quaternion make(int_c a, int_c b, int_c c, int_c d){
  return quaternion({a, b, c, d});
}

quaternion operator*(quaternion a, quaternion b){
  return make(
      a[0] * b[0] + a[1] * b[2],
      a[0] * b[1] + a[1] * b[3],
      a[2] * b[0] + a[3] * b[2],
      a[2] * b[1] + a[3] * b[3]);
}

quaternion operator-(quaternion a){
  return make(-a[0], -a[1], -a[2], -a[3]);
}

const quaternion E = make(int_c(1, 0), int_c(0, 0), int_c(0, 0), int_c(1, 0));
const quaternion I = make(int_c(0, 1), int_c(0, 0), int_c(0, 0), int_c(0, -1));
const quaternion J = make(int_c(0, 0), int_c(1, 0), int_c(-1, 0), int_c(0, 0));
const quaternion K = make(int_c(0, 0), int_c(0, 1), int_c(0, 1), int_c(0, 0));

quaternion pow(quaternion q, ll x){
  quaternion res = E;
  x %= 4;
  if(x > 0) res = res * q;
  if(x > 1) res = res * q;
  if(x > 2) res = res * q;
  return res;
}

const int MAXL = 1000005;
int T, L;
ll X;
string _S, S;
quaternion Q[MAXL];

quaternion get(char c){
  if(c == 'i') return I;
  if(c == 'j') return J;
  if(c == 'k') return K;
  return E;
}

int main(){
  cin >> T;
  for(int _t = 1; _t <= T; _t++){
    cin >> L >> X >> _S;
    S = "";
    for(int i = 0; i < min(X, 100LL); i++){
      S = S + _S;
    }
    Q[0] = E;
    int res = 0;
    for(int i = 0; i < S.size(); i++){
      Q[i + 1] = Q[i] * get(S[i]);
      if(res == 0 && Q[i + 1] == I) res += 1;
      if(res == 1 && Q[i + 1] == K) res += 1;
    }
    printf("Case #%d: ", _t);
    cout << (res == 2 && pow(Q[L], X) == -E ? "YES\n" : "NO\n");
  }
}
