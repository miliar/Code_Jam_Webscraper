#include <bits/stdc++.h>

#define forn(i,n) for(int i = 0; i < n; i++)

using namespace std;

void exDigits(long long int n, bool * digits){

    while(n != 0){
        digits[n%10] = true;
        n /= 10;
    }

}

int sheep (long long int n){

    if(n == 0) return -1;
    bool digits[10]; 
    int m = 0;
    forn(i, 10) digits[i] = false;

    bool res = false;

    while(!res){
        m++;
        exDigits(n*m, digits);
        res = true;
        forn(i,10){
            if(!digits[i]) res = false;
        }
    }

    return n*m;


}

int main(){

    int testCases, res;
    long long int n;
    string ans;

    cin >> testCases;
    forn(tt, testCases){

        cin >> n;

        res = sheep(n);
        if(res == -1) ans = "INSOMNIA";
        else ans = to_string(res);

        cout << "Case #" << tt + 1 << ": " << ans << endl;

    }

    return 0;
}