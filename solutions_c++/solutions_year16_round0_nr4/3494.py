#include <iostream>
#include <string>
using namespace std;

int main() {
    freopen("/Users/koushikroy/Desktop/algos/Toph-Contest/inp.txt","r",stdin);
    freopen("/Users/koushikroy/Desktop/algos/Toph-Contest/out.txt","w",stdout);
    int T,N,K,S;
    cin >> T;
    for(int k = 0; k < T; k++){
        cin >> N >> K >> S;
        
        cout << "Case #" << k+1 << ": ";
        cout << 1 ;
        for(int l = 2; l <= S; l++){
            cout << " " << l;
        }
        cout << endl;
        
        
    }
}