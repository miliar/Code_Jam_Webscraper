#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int mult[4][4] = {{0,1,2,3}, {1,0,3,2}, {2,3,0,1}, {3,2,1,0}};
int sign[4][4] = {{1,1,1,1}, {1,-1,1,-1}, {1,-1,-1,1}, {1,1,-1,-1}};

struct quat{
  int symb;
  int sign;
};

quat multiply(quat x, quat y) {
  quat result;
  result.symb = mult[x.symb][y.symb];
  result.sign = x.sign*y.sign*sign[x.symb][y.symb];
  return result;
}

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int T;
  scanf("%d", &T);


  for (int t=1; t<=T; ++t) {
    printf("Case #%d: ", t);
    int L, X;
    cin >> L >> X;
    X = min(X, 12+(X%4));
    int length = L*X;
    char str[1000000];
    cin >> str;
    quat ijk[length];
    for (int i=0; i<L; ++i) {
      char x = str[i];
      int num;
      switch(x) {
        case 'i': num = 1; break;
        case 'j': num = 2; break;
        case 'k': num = 3; break;
      }
      for (int j=0; j<X; ++j) {
        ijk[j*L+i].symb = num;
        ijk[j*L+i].sign = 1;
      }
    }
    bool success = false;
    quat q; q.sign = 1; q.symb = 0;
    int i;
    for (i=0; i<length-2; ++i) {
      q = multiply(q, ijk[i]);
      if (q.sign==1 && q.symb==1) break;
    }  
    if (i<length-2) {
      q.sign = 1; q.symb = 0;
      int j;
      for (j=length-1; j>i+1; --j) {
        q = multiply(ijk[j], q);
        if (q.sign==1 && q.symb==3) break;
      }  
      if (j>i+1) {
        q.sign=1; q.symb=0;
        for (int k=i+1; k<j; ++k) q = multiply(q, ijk[k]);
        if (q.sign==1 && q.symb==2) success = true;
      }
    }
    if (success) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
}
