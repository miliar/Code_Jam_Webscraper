
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;


bool ok(vector<int> &v) {
  int pos = 0;
  for(; pos+1 < v.size(); pos++) if(v[pos] > v[pos+1]) break;
  for(; pos+1 < v.size(); pos++) if(v[pos] < v[pos+1]) return false;
  return true;
}

int nb(vector<int> &v) {
  int nb = 0;
  for(int i = 0; i < v.size(); i++)
    for(int j = i+1; j < v.size(); j++)
      if(v[i] > v[j]) nb++;
  return nb;
}



int main() {
	int T;	
	cin >> T;



  for(int t = 1; t <= T; t++) {
    int best = 1000000000;

    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++) cin >> A[i];

  /*  vector<int> V(N);
    for(int i = 0; i < N; i++) V[i] = i;

    do {
      vector<int> V2(N);
      for(int i = 0; i < N; i++) V2[i] = A[V[i]];
      if(ok(V2)) if(nb(V) < best) {
        best = nb(V);
        for(int i = 0; i < N; i++) cout << V2[i] << " ";
        cout << endl;
        for(int i = 0; i < N; i++) cout << V[i] << " ";
        cout << endl;
        for(int i = 0; i < N; i++) cout << A[i] << " ";
        cout << endl << nb(V) << endl;
      }
    }
    while(next_permutation(V.begin(), V.end()));
*/

    int nb = 0;
    while(A.size() > 0) {
      int pos_min = 0;
      for(int i = 0; i < A.size(); i++) 
        if(A[i] < A[pos_min]) pos_min = i;
      nb += min(pos_min, (int)A.size() - 1 - pos_min);
      A.erase(A.begin() + pos_min);
    }



    /*

       vector<int> inv1(N+1), inv2(N+1);
       inv1[0] = 0;
       inv2[N] = inv2[N-1] = 0;
       for(int i = 1; i < N; i++) {
       inv1[i] = inv1[i-1];
       for(int j = 0; j < i; j++) if(A[j] > A[i]) inv1[i]++;
       inv2[N-1-i] = inv2[N-i];
       for(int j = N-i; j < N; j++) if(A[j] > A[N-1-i]) inv2[N-1-i]++;
       }
       for(int i = 0; i < N; i++) if(inv1[i] + inv2[i+1] < best) best = inv1[i] + inv2[i+1];
       */
    cout << "Case #" << t << ": " << nb << endl;
  }


}
