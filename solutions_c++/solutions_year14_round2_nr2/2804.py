#include <iostream>

using namespace std;

int main(void){
    int T; cin >> T;
    //cout << T << endl;
    
    for(int t = 0; t < T; t++){
        unsigned long A, B, K;
        cin >> A >> B >> K;
        //cout << ">A:" << A << " B:" << B << " K:" << K << endl;

        unsigned int count = 0;
        for (unsigned int a = 0; a < A; ++a){
            for (unsigned int b = 0; b < B; ++b){
                unsigned int x = a & b;
                if (x < K) {
                    ++count;
                }
            }
        }
        cout << "Case #" << t + 1 << ": " << count << endl;
    }

    return 0;
}
