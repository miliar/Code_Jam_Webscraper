#include "mylib.h"


// "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
// Z-0 X-6 

void fix(vla<int> &a, vla<int> &v, char c, int val, charp s) {
  int count=v[c];
  if (0==count) return;
  a[val]=count;
  charp t=s;
  while (*t) {
    char i=*t++;
    v[i]=v[i]-count;
  }
}

string solve(string w) {
  ccharp s=w.c_str();
  // A-Z 0..25
  vla<int> v('Z'+1, 0);
  charp t=(charp)s;
  while (*t) {
    char c=*t++;
    v[c]=v[c]+1;
  }
  // v.dump();
  vla<int> a(10, 0);
  fix(a, v, 'Z', 0, "ZERO");
  fix(a, v, 'W', 2, "TWO");
  fix(a, v, 'U', 4, "FOUR");
  fix(a, v, 'X', 6, "SIX");
  fix(a, v, 'O', 1, "ONE");
  fix(a, v, 'S', 7, "SEVEN");
  fix(a, v, 'F', 5, "FIVE");
  fix(a, v, 'R', 3, "THREE");
  fix(a, v, 'T', 8, "EIGHT");
  fix(a, v, 'I', 9, "NINE");

  ostringstream res;
  for (int i=0; i<=9; i++) {
    for (int k=0; k<a[i]; k++) {
      res<<(char)('0'+i);
    }
  }
  return res.str();
}

int solve_all(mifstream &fi, mofstream &fo) {
  int count=fi.nextInt();
  for (int i=1; i<=count; i++) {
    string result=solve(fi.nextString());
    fo<<"Case #"<<i<<": "<<result<<endl;
  }
  return 0;
}

