#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int CASE = 1; CASE <= T; CASE++){
        int N, multi = 0;
        cin >> N;
        cout << "Case #" << CASE <<": ";
        
        array<bool,10> arr = {};
        int remaining = 10;
        
        if (N == 0){
            cout << "INSOMNIA" << endl;
            continue;
        }

        do {
            multi += N;
            int temp = multi;
            while(temp){
                const int digit = temp % 10;
                temp /= 10;
                if (!arr[digit]){
                    arr[digit] = true;
                    remaining--;
                }
            }
        } while(remaining);
        cout << multi << endl;
    }
    return 0;
}
