#include <iostream>
#include <set>
#include <stack>

#define REPEAT 100000
using namespace std;
typedef set<int> S;
typedef pair<int, int> P;
typedef stack<P > SP;

int main(){
  int T = 0;
  cin >> T;

  for(int t = 0; t < T; ++t){
    int N = 0;
    cin >> N;
    double nb[N];
    double kb[N];
    for(int i = 0; i < N; ++i){
      cin >> nb[i];
    }
    for(int i = 0; i < N; ++i){
      cin >> kb[i];
    }
    sort(nb, nb + N);
    sort(kb, kb + N);

    // war
    int in = 0;
    int ik = -1;
    for(int i = 0; i < N; ++i){
      //cout << nb[i] << " " << kb[i] << endl;
    }
    //cout << "-----" << endl;
    while(ik < N && in < N){
      ik++;
      while(nb[in] > kb[ik]) ik++;
      //cout << nb[in] << " " << kb[ik] << endl;
      if(ik < N){
        in++;
      }
    }
    int war = (N-in);

    sort(nb, nb + N, greater<double>());
    sort(kb, kb + N, greater<double>());

    in = 0;
    ik = -1;
    while(ik < N && in < N){
      ik++;
      while(nb[in] < kb[ik]){
        ik++;
      }
      if(ik < N){
        in++;
      }
    }
    int dwar = in;
    cout << "Case #" << (t+1) << ": " << dwar << " " << war << endl;
  }
}
