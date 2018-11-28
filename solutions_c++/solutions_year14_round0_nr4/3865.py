#include <set>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int n;
double A[1000], B[1000];

int Solve1() {
  sort(A,A+n);
  sort(B,B+n);
  for (int k=n; k>=0; --k) {
    bool ok=true;
    for (int i=0; i<k; ++i)
      if (B[i] > A[n-k+i]) ok=false;
    if (ok) return k;
  }
  

  //int i=0;
 // while (i<n && A[n-i-1] > B[i]) ++i;
  //return i;
}

int Solve2() {
  set<double> S;
  for (int i=0;i<n;++i) S.insert(B[i]);
  int c=0;
  for (int i=0;i<n;++i)
    if (S.lower_bound(A[i]) == S.end()) {
      c++;
      S.erase(S.begin());
    } else {
      S.erase(S.lower_bound(A[i]));
 
    }
  return c;
}

int main (){
  int Z;
  cin >> Z;
  for (int z=1;z<=Z;++z) {
    cin >> n;
    for (int i =0;i<n;i++) 
      cin>>A[i];
    for (int i =0;i<n;i++) 
      cin>>B[i];
    cout << "Case #" << z << ": " << Solve1() << " " << Solve2() << endl;
  }
  return 0;
}

