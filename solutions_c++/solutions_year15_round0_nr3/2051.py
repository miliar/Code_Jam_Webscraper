/*
ID: jeffrey31
LANG: C++
TASK: C
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
//0 = 1, 1 = i, 2 = j, 3 = k
const int N = 10010;
int mult[4][4] = {{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
int sgn[4][4] = {{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
struct quat {
  double q[4];
  quat() {
    q[0] = q[1] = q[2] = q[3] = 0;
  }
  quat(double q0, double q1, double q2, double q3) {
    q[0] = q0;
    q[1] = q1;
    q[2] = q2;
    q[3] = q3;
  }
  quat operator *(quat& b) {
    quat ret(0,0,0,0);
    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
        int idx = mult[i][j];
        double coef = q[i] * b.q[j] * (sgn[i][j]);
        ret.q[idx] += coef;
      }
    }
    return ret;
  }
  bool operator ==(quat &b) {
    return q[0] == b.q[0] && q[1] == b.q[1] && q[2] == b.q[2] && q[3] == b.q[3];
  }
  quat inverse() {
    quat ret(q[0],q[1],q[2],q[3]);
    double mag = 0;
    for(int i = 0; i < 4; i++) {
      mag += q[i]*q[i];
    }
    ret.q[0] /= mag;
    ret.q[1] *= -1/mag;
    ret.q[2] *= -1/mag;
    ret.q[3] *= -1/mag;
    return ret;
  }
} arr[N], pp[N], u[4];
int t;
int main() {
  freopen("C.in","r",stdin);
  freopen("C.out","w", stdout);
  cin >> t;
  
  for(int l,x,i = 1; i <= t; i++) {
    string lin;
    for(int ii = 0; ii < 4; ii++) {
      quat cur(0,0,0,0);
      cur.q[ii] = 1;
      u[ii] = cur;
    }

    printf("Case #%d: ", i);
    cin >> l >> x;
    cin >> lin;
    pp[0] = u[0];
    int f1 = -1, f2 = -1;
    for(int j = 1; j <= l*x; j++) {
      int idx = lin[((j-1) + l) % l]-'h';
      pp[j] = pp[j-1] * u[idx];
      if(f1 == -1 && pp[j] == u[1] )
        f1 = j;
      if(pp[j] == u[3]) {
        f2 = j;
      }
    }
    quat en(-1,0,0,0);
    cout << ((pp[l*x] == en && f1 != -1 && f1 < f2)? "YES" : "NO") << endl;
  }


  return 0;
}