#include<iostream>
#include<vector>
using namespace std;



int main() {
    
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    int rounds;
    cin >> rounds;

    long long  N;
    for (int j = 0; j < rounds; ++j){
          cin >> N;
          vector<int> V(10);
          cout << "Case #" << j+1 << ": ";
          if (N == 0) cout << "INSOMNIA" << endl;
          else {
              int conta = 0;
              int it = 1;
              while(conta < 10) {
                      long long aux_N = N*it;
                      while(aux_N > 0) {
                            if (V[aux_N%10] == 0) {
                               ++conta;
                               V[aux_N%10] = 1;
                            }
                            aux_N /= 10;
                      }
                      ++it;
              }
              cout << N*(it-1) << endl;
          }
          
    }
}
