#include <iostream>
using namespace std;
bool verify(bool arr[]);
int main() {
    int cases, input, output, rem;
    cin >> cases;
    for (int i = 1; i <= cases; ++i) {

//=======================================================================

        bool arr[10];
        for (int j = 0; j < 10; ++j)
            arr[j] = false;
        cin >> input;
        if(input == 0) {
            cout << "Case #" << i << ": " << "INSOMNIA" << '\n';
            continue;
        }
        int N = 1;
        int input_calc;
        // At this point, we have input in input
        while(verify(arr) != true) {
            input_calc = input * N;
            output = input_calc;
            while (input_calc != 0) {
                rem = input_calc % 10;
                arr[rem] = true;
                input_calc /= 10;
            }
            N++;
        }

        cout << "Case #" << i << ": " << output << '\n';
    }

//=======================================================================

}

bool verify(bool arr[]) {
    for (int i = 0; i < 10; ++i) {
        if (arr[i] == false)
            return false;
    }
    return true;
}
