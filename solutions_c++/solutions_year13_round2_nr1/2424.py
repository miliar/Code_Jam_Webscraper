#include <cmath>
//#include <gmp.h>
//#include <gmpxx.h>
#include <iomanip>
#include <iostream>
#include <vector>


using namespace std;

int f(int x) {


}

/**
*  Insertion Sort; A sorting algorithm which will order an arbitrary array of items.
*/
template <class elemType>
void insertionSort(vector<elemType> &list, int length) {
    for (int firstOutOfOrder = 1; firstOutOfOrder < length;
            firstOutOfOrder++) {
        if (list[firstOutOfOrder] < list[firstOutOfOrder - 1]) {
            elemType temp = list[firstOutOfOrder];
            int location = firstOutOfOrder;
            do {
                list[location] = list[location - 1];
                location--;
            } while(location > 0 && list[location - 1] > temp);
            list[location] = temp;
        }
    }
} //end insertionSort

int main( void ) {
    int T;
    cin >> T;
    for(int k = 1; k <= T; ++k) {
        unsigned long long A, AO;
        int N, operations = 0, otherOperations = 0;
        vector<int> motes;
        cin >> A >> N;
        AO = A;
        for(int i = 0; i < N; ++i){
            int m;
            cin >> m;
            motes.push_back(m);
        }
        insertionSort(motes, motes.size());
       for(int i = 0; i < N; ++i){
            if(motes.at(i) < A){
                A += motes.at(i);
            }else if(motes.at(i) < 2*A - 1){
                A += A - 1 + motes.at(i);

                ++operations;
            }else{
                operations += N-i;
                break;
            }
       }
       for(int i = 0; i < N; ++i){
         if(motes.at(i) < AO){
                AO += motes.at(i);
            }else if(AO != 1){
                while(AO <= motes.at(i)){
                    AO = 2*AO - 1;
                    ++otherOperations;
                }
                AO += motes.at(i);
            }else{
                otherOperations += 101;
                break;
            }
       }
        int answer = (operations < otherOperations) ? operations : otherOperations;
        cout << "Case #" << k << ": " << answer << endl;
    }

    return 0;
}
