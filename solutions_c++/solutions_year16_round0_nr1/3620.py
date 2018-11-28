#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

void addDigits(unsigned long long n, int& counter, vector<bool>& digits){
    unsigned long long power = 1;
    while(power <= n){
        power *= 10;
    }
    if(power > n) power /= 10;
    while(power > 0){
        if(digits[(n/power)%10] == false) counter++;
        digits[(n/power)%10] = true;
        power /= 10;
    }
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=0; i<t; i++){
        unsigned long long n = 0;
        cin >> n;
        vector<bool> digits(10, false);
        int nbDigits = 0;
        addDigits(n, nbDigits, digits);
        unsigned long long j=2;
        for(; j<=10000; j++){
            addDigits(n*j, nbDigits, digits);
            if(nbDigits == 10) break;
        }
        cout << "Case #" << i+1 << ": ";
        if(nbDigits == 10) cout << n*j;
        else cout << "INSOMNIA";
        cout << endl;
    }
    return 0;
}
