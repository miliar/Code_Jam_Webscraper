#include<iostream>
#include<cmath>
#include<cstring>

using namespace std;

const int I=2;
const int J=3;
const int K=4;

int M[4][4]={{1, I, J, K},{I, -1, K, -J},{J, -K, -1, I},{K, J, -I, -1}};

class quaternion {
  int val;
  int sig;
public:
  quaternion() {
    val=1;
    sig=1;
  }
  quaternion(int v) {
    val=abs(v);
    sig=(v<0)?-1:1;
  }
  quaternion(int v, int s) {
    val=v;
    sig=s;
  }
  quaternion(char c) {
    sig=1;
    if (c=='1') val=1;
    else val=(int)(c-'i'+2);
  }

  quaternion& operator=(int v) {
    val=abs(v);
    sig=(v<0)?-1:1;
    return *this;
  }
  quaternion operator-() const {
    quaternion r(val, -sig);
    return r;
  }
  bool operator==(const quaternion &other) const {
    return ((val==other.val) && (sig==other.sig));
  }

  quaternion operator*(const quaternion &other) const {
    return (quaternion)(M[val-1][other.val-1]*(sig*other.sig));
  }
  quaternion& operator++() {
    if (val==1 || val==K) val=1;
    else ++val;
    return *this;
  }

  void print() {
    string s=(sig<0)?"-":"";
    if (val==1)s+="1";
    else if (val==I)s+="i";
    else if (val==J)s+="j";
    else if (val==K)s+="k";
    else {cerr << "Error\n"; return;}
    cout << s << endl;
  }
};

bool solve_it(char *s, int cx) {
  quaternion cu(1), luq(I);
  for (int x=0; x<cx; ++x) {
    for (char *re=s; *re!=0; re++) {
      quaternion ncu, ne(*re);
      ncu=cu*ne;
      if (luq==ncu) {
	cu=1;
	++luq;
      } else cu=ncu;
    }
  }
  return (luq==cu);
  /*   quaternion ncu, ne(*re);
      ncu=cu*re;
      if (ncu==luq) {
  */
}

bool solve(int lu, quaternion cu, char *s, char *re, int cx) {
  if (re[0]==0) {
    if (cx<=1) return false;
    else return solve(lu, cu, s, s, cx-1);
  }
  quaternion luq(lu), ncu, ne(re[0]);
  ncu=cu*ne;
  if (luq==ncu) {
    if (lu==K) return true;
    else return (solve(lu+1, (quaternion)1, s, re+1, cx));
  }
  if (solve(lu+1, (quaternion)1, s, re+1, cx)) return true;
  return solve(lu, ncu, s, re+1, cx);
} 


int main() {
  unsigned int T;
  cin >> T;

  for (unsigned int t=1; t<=T; ++t) {
    string y="NO";
    int L, X;
    string s;
    cin >> L >> X;// >> s;
    char cs[L+1];
    cin >> cs;
    /*strcpy(cs, s.c_str());
    for (int x=1; x<X; ++x)
      strcat(cs, s.c_str());
    */
    //if (solve(I, (quaternion)1, cs, cs, X)) y="YES";
    if (solve_it(cs, X)) y="YES";
    cout << "Case #" << t << ": " << y << endl;
  }

  return 0;
}
