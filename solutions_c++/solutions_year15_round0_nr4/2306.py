#include <bits/stdc++.h>
using namespace std;

bool foo(int r, int c, int x){
  return (r * c) % x;
}

int main(){
  freopen("D-small.in", "r", stdin);
  freopen("D-small.out", "w", stdout);
  int tc, ct = 0;
  cin >> tc;
  while (tc--){
    int x, r, c;
    string wi, ri = "RICHARD", ga = "GABRIEL";
    cin >> x >> r >> c;
    if (x == 1){
      wi = ga;
    }
    if (x == 2){
      (foo(r, c, x))? wi = ri: wi = ga;
    }
    if (x == 3){
      if (!foo(r, c, x) && (r == 1 || c == 1))
        wi = ri;
      else if(!foo(r, c, x) && !(r == 1 || c == 1))
        wi = ga;
      else
        wi = ri;
    }
    if (x == 4){
      if (!foo(r, c, x))
        (r <= 2 || c <= 2)? wi = ri: wi = ga;
      else
        wi = ri;
    }
    cout << "Case #" << ++ct << ": " << wi << endl;
  }
}
