#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

struct Mat{
  int v[3][3];
};

Mat clear = {};
Mat m[2] = {{},{}};

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;

    string pp = "P", rr="R", ss="S";
    
    m[0] = clear;
    m[0].v[0][0] = 1;
    m[0].v[1][1] = 1;
    m[0].v[2][2] = 1;

    for (int i=0;i<n;i++) {
      string tp = pp, tr = rr, ts = ss;

      pp = tp + tr;
      m[1].v[0][0] = m[0].v[0][0] + m[0].v[1][0];
      m[1].v[0][1] = m[0].v[0][1] + m[0].v[1][1];
      m[1].v[0][2] = m[0].v[0][2] + m[0].v[1][2];

      rr = tp + ts;
      m[1].v[1][0] = m[0].v[0][0] + m[0].v[2][0];
      m[1].v[1][1] = m[0].v[0][1] + m[0].v[2][1];
      m[1].v[1][2] = m[0].v[0][2] + m[0].v[2][2];

      ss = tr + ts;
      m[1].v[2][0] = m[0].v[1][0] + m[0].v[2][0];
      m[1].v[2][1] = m[0].v[1][1] + m[0].v[2][1];
      m[1].v[2][2] = m[0].v[1][2] + m[0].v[2][2];

      swap(m[0], m[1]);
      //cout << pp << "," << rr << "," << ss << endl;
      //for (int i=0;i<3;i++) {
      //  cout << m[0].v[i][0] << " " << m[0].v[i][1] << " " << m[0].v[i][2] << endl;
      //}
    }

    string str[3] = {pp, rr, ss};
    cout << "Case #" << t << ": ";
    for (int i=0;i<4;i++) {
      if (i==3) {
        cout << "IMPOSSIBLE";
      }
      else if (m[0].v[i][0] == p && m[0].v[i][1] == r && m[0].v[i][2] == s)
      {
        cout << str[i];
        break;
      }
    }
    cout << endl;


    //printf("Case #%d: %d\n", t, kn);
  }

}
