#include <iostream>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

#define SIZE 100000

int main() {

    int T, counter;
    double C, F, X, rate;
    double arr1[SIZE], arr2[SIZE];

    cin >> T;
    
    arr1[0] = arr2[0] = 0;
    for (int i = 0; i < T; i++) {
        
        cin >> C >> F >> X;
        
        counter = 1;
        rate = 2;
        while (1) {
            arr1[counter] = arr1[counter-1] + (C/rate);
            arr2[counter] = arr1[counter-1] + (X/rate);
            rate += F;

            if ( (arr2[counter] > arr2[counter-1]) && (counter != 1) ) {
                cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << arr2[counter-1] << endl;
                break;
            }
            counter++;
        }
    }

    return 0;
}
