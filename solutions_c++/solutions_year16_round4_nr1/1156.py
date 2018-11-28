#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>

using namespace std;

vector<int> lineup;
//1 = P, 2= R, 3 = S
//1 beats 2 beats 3 beats 1
int N,P,R,S;
int n2;

int result(int a,int b){
  if (a == 1) {
    if (b == 2) return a;
    if (b == 3) return b;
  }

  if (a == 2) {
    if (b == 3) return a;
    if (b == 1) return b;
  }
  if (a == 3) {
    if (b == 1) return a;
    if (b == 2) return b;
  }
  return -1;
}

list<int> genP(int depth);
list<int> genR(int depth);
list<int> genS(int depth);

list<int> genP(int depth) {
  if (depth == 0) {
    return list<int>(1,1);
  } else {
    list<int> l1 = genP(depth-1);
    list<int> l2 = genR(depth-1);
    if (l1 < l2) {
      l1.splice(l1.end(),l2);
      return l1;
    } else {
      l2.splice(l2.end(),l1);
      return l2;
    }
  }
}

list<int> genR(int depth) {
  if (depth == 0) {
    return list<int>(1,2);
  } else {
    list<int> l1 = genR(depth-1);
    list<int> l2 = genS(depth-1);
    if (l1 < l2) {
      l1.splice(l1.end(),l2);
      return l1;
    } else {
      l2.splice(l2.end(),l1);
      return l2;
    }
  }
}

list<int> genS(int depth) {
  if (depth == 0) {
    return list<int>(1,3);
  } else {
    list<int> l1 = genP(depth-1);
    list<int> l2 = genS(depth-1);
    if (l1 < l2) {
      l1.splice(l1.end(),l2);
      return l1;
    } else {
      l2.splice(l2.end(),l1);
      return l2;
    }
  }
}

void count(list<int> &x,int &p,int &r,int &s) {
  p = 0;
  r = 0;
  s = 0;
  for (auto &v : x) {
    if (v == 1) p++;
    if (v == 2) r++;
    if (v == 3) s++;
  }
}

int main() {
  int T;
  cin >> T;
  vector<char> out = {' ','P','R','S'};
  for (int t = 1;t <= T;t++) {
    cin >> N >> R >> P >> S;
    n2 = 1 << N;
    bool ok = false;
    list<int> x;
    int r,p,s;
    
    x = genP(N);
    count(x,p,r,s);
    if (R == r && P == p && S == s) {
      lineup = vector<int>(x.begin(),x.end());
      ok = true;
    }
    if (!ok) {
      x = genS(N);
      count(x,p,r,s);
      if (R == r && P == p && S == s) {
        lineup = vector<int>(x.begin(),x.end());
        ok = true;
      }
    }
    if (!ok) {
      x = genR(N);
      count(x,p,r,s);
      if (R == r && P == p && S == s) {
        lineup = vector<int>(x.begin(),x.end());
        ok = true;
      }
    }
    if (ok) {
      printf("Case #%d: ",t);
      for (int i = 0;i < n2;i++) {
        cout << out[lineup[i]];
      }
      cout << endl;

    } else {
      printf("Case #%d: IMPOSSIBLE\n",t);
    }
  }
}
