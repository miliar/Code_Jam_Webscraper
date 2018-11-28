#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int arr[10];

void getDigits(int num, int &cnt) {
    while (num) {
        int rem = num % 10;
        if (!arr[rem]) {
            arr[rem] = 1;
            ++cnt;
        }
        
        num /= 10;
    }
}

int main() {
    freopen("CountingSheep.in", "rt", stdin);
    freopen("CountingSheep.out", "wt", stdout);
    int numTests;
    cin >> numTests;

    
    for (int i = 0; i < numTests; ++i) {
        memset(arr, 0, sizeof(arr));
        int N;
        cin >> N;
        
        if (N  == 0) {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        int cnt = 0;
        getDigits(N, cnt);
        
        int num = N;
        while (cnt < 10) {
            num += N;
            getDigits(num, cnt);       
        }
        
        cout << "Case #" << i + 1 << ": " << num << endl;
    }
    
    return 0;
}
