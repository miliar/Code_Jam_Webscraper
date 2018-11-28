#include <stdio.h>
#include <iostream>
#include <inttypes.h>
#include <vector>
using namespace std;

void checkDigit(int64_t N, bool * digit_map) {
    while (N > 0) {
        digit_map[N%10] = true;
        N /= 10;
    }
}

bool checkTenDigit (bool * digit_map){
    for (int i = 0; i < 10; ++i) {
        if (!digit_map[i]) {
            return false;
        }
    }
    return true;
}

void printEnd(int64_t N) {
    if (N == 0) {
        cout<<"INSOMNIA";
        return ;
    }
    bool digit_map[10] = {false};
    int64_t current = N;
    while (true) {
        checkDigit(current, digit_map);
        if(checkTenDigit(digit_map)) {
            cout<<current;
            return ;
        }
        current += N;
    }
    
}


int main() {
    
    int T;
    cin >> T;
    vector<int64_t> input;
    for (int i = 0; i < T; i++) {
        int64_t temp; cin>>temp;
        input.push_back(temp);
    }
    
    for (int i = 0; i < T; i++) {
        cout<<"Case #"<<i+1<<": ";
        printEnd(input[i]);
        cout<<"\n";
    }
    
    
    return 0;
}