//#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream cin("A-large.in");
ofstream cout("A-large.out");

int main() {
    int T;
    cin >> T;
    int A[1001];
    for (int t=0; t<T; t++) {
      int smax; string s;
      cin >> smax >> s;
      for (int i=0; i<=smax; i++) { A[i] = (s[i]-48); }
      long long curn = A[0]; long long extra = 0;
      for (int i=1; i<=smax; i++) if (curn >= i) curn += A[i]; else { extra += 1; curn+=1+A[i]; }
      cout << "Case #" << t+1 << ": " << extra << endl;
    }
return 0;
}
