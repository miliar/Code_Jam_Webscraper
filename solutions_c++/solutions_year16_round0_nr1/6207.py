#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

bool markDigits(long long n, bool* digits){
    if(n == 0){
        digits[0] = true;
    }

    while(n){
        digits[n % 10] = true;
        n /= 10;
    }

    for(int i = 0; i < 10; i++){
        if(!digits[i]){
            return false;
        }
    }

    return true;
}

long long solve(long long n){
    bool digits[10];
    memset(digits, false, sizeof(digits));

    long long orgN = n;
    while(true){
        if(markDigits(n, digits)){
            return n;
        }

        n += orgN;
        if(n == orgN){
            break;
        }
    }

    return -1;
}

int main(){
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    int t;
    long long n;
    cin >> t;
    for(int c = 1; c <= t; c++){
        cin >> n;
        cout << "Case #" << c << ": ";
        int sol = solve(n);
        if(sol < 0){
            cout << "INSOMNIA" << endl;
        }
        else{
            cout << sol << endl;
        }
    }

    return 0;
}