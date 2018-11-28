#include <iostream>
#include <stdint.h>

using namespace std;

int main() {
    int t = 0;
    cin >> t;
    for (int i=1; i<=t; ++i){
        uint64_t N;
        cin >> N;
        //N = i;
        if(N == 0){
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        } else {
            int done = 0b1111111111;
            uint64_t jN = 0;
            while (done != 0){
                jN += N;
                for (uint64_t temp = jN; temp != 0; ) {
                    done = done & ~(1 << (temp % 10));
                    temp = temp / 10;
                }
            }
            cout << "Case #" << i << ": " << jN << endl;
        }
    }
}