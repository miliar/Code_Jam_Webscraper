#include<iostream>
using namespace std;

int main(){
    int T, A, B, K;
    cin >> T;
    unsigned int t, a, b, k;
    for(t = 1; t <= T; t++){
          cin >> A >> B >> K;
          k = 0;
          for(a = 0; a < A; a++){
                for(b = 0; b < B; b++){
			//cout << (a & b) << endl;
                      if((a & b) < K){
                              k++;
                              //cout << t << T << endl;
                             // cout << a <<" " << b << endl; 
                      }
                }
          }
          cout << "Case #" << t << ": " << k << endl;
    }
    //system("pause");
    return 0;
}
