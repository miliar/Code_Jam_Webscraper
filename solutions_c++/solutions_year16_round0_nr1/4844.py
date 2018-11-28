#include <iostream> 
#include <vector>
#include <math.h>
using namespace std; 

int decompt(int n, vector<bool>& vu, int nbv){
  while (n != 0){
    double upn = floor(n/10)*10;
    int d = n - upn;
    if (!vu[d]){
      vu[d] = true;
      nbv++;
    }
    n = upn / 10;
  }
  return nbv;
}

int main(){
  int T, nbv;
  cin >> T;  
  for (int i = 1; i <= T; ++i) {
    double N, Nc;
    cin >> N;
    Nc = N;
    if (N == 0){
      cout << "Case #" << i << ": INSOMNIA"  << endl;
    }
    else{
      vector<bool> vu(10, false);
      nbv = decompt(N, vu, 0);
      while (nbv != 10){
       /* cout << Nc << endl;
        for (int i = 0; i<10; ++i){
          cout << vu[i] << ' ';
        }
        cout << endl;
        cout << nbv << endl;*/
        Nc = Nc + N;
        nbv = decompt(Nc, vu, nbv);
      }
      int nf = Nc;
      cout << "Case #" << i << ": " << nf  << endl;
    }
  }
}
