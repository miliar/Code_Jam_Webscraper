#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

void input(int N, vector<double>& A) {
  int i;
  double x;
  fr (i, N) {
    cin >> x;
    A.pb(x);
  }
  sort(A.begin(), A.end());
}

int proc(vector<double>&A, vector<double>& B) {
  int res = 0, a = 0, b = 0;
  while (a < SZ(A)) {
    if (A[a] > B[b]) {
      res++;
      b++;
    }

    a++;
  }
  return res;
}

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    int N;
    vector<double> A, B;
    cin >> N;
    input(N, A);
    input(N, B);
    cout << "Case #" << cn << ": ";
    cout << proc(A, B) << " " << N - proc(B, A) << endl;
  }
  return 0;
}
