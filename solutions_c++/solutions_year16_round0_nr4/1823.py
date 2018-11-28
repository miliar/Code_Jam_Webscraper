#include <iostream>
#include <cstdint>

using namespace std;

uint64_t lpow(long long a, int e) {
    if(e <= 0)
        return 1;
    uint64_t h = lpow(a, e/2);
    return h * h * ((e&1)? a : 1);
}

void comp(int tc){
    int K, C, S;
    cin >> K >> C >> S;
    
    uint64_t e = lpow(K, C-1);
    cout << "Case #" << tc << ": ";
    for(int i=0; i<S; ++i){
        cout << (1 + e * i) << " ";
    }
    cout << endl;
}

int main(){
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i){
        comp(i);
    }
}