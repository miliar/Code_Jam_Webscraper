#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  
    int T;
    
    cin >> T;
    char S[1010];
    int Smax;
    
    for (int _i = 0 ; _i < T; _i++){
        cout << "Case #"<<_i+1<<": ";
        cin >> Smax;
        cin >> S;
        int sum = 0;
        int friends = 0;
        for (int i = 0 ; i < Smax+1 ; i++) {
            int Sc = (int)S[i] - '0';
            while (i > sum && Sc != 0) {
                friends++;
                sum++;
            }
            sum += Sc;
        }
        cout << friends << endl;
        
        
    }
    
    return 0;
}

