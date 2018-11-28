#include <iostream>
#include <stdint.h>
using namespace std;
 
int main() {
int T,S,x;
int W;
  // T- ile testow, S- najwysza shyness, B - ciag ilosciowy, x-pomocniczy, W-wynik (ile osob trzeba doprosic);
 
char B[1001];
int t[1001];
int C; //suma ludzi ktorzy wstali do tej pory;
 
 
ios_base::sync_with_stdio(false);
 
    cin >> T;
    for(int i = 0; i < T; i++) {
       cin >> S;
       cin >> B;
       for (int j=0; j<S+1; j++){
    t[j] = B[j] - '0';
}
   C=t[0];
   W=0;
                  for(int k=1;k<S+1; k++){
                 
                    if (t[k]!=0){
                    if (k>C){
                      while (k>C){
                        W++;
                        C++;
                      }
                      C=C+t[k];
                      }
                      else C=C+t[k];
                     
                     
                    }
                  }
                  cout << "Case #" << i+1 << ':'<< ' ' << W << '\n';
    }
   
   
 
  return 0;
}
