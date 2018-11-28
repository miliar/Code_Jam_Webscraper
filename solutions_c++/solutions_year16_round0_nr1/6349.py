#include <bits/stdc++.h>
using namespace std;

bool isFull(vector<int> digits) {
    for(int i=0; i<digits.size(); i++) {
        if(digits[i] == 0)
            return false;
    }
    return true;
}

main() {

    int nCases, n, temp, k;
    bool cond;
    string number;

    cin >> nCases;

    for(int i=0; i<nCases; i++){
        vector<int> digits(10, 0);
        cond = false;
        k = 1;
        cin >> n;
        cout << "Case #" << i+1 << ": ";
        if(n != 0) {
            while(!cond) {
                temp = n*k;
                number = to_string(temp);
                for(int j=0; j<number.size(); j++) {
                    digits[number[j] - '0']++;

                }
                cond = isFull(digits);

                if(!cond){
                    k++;
                }
            }
            cout << temp << '\n';
        } else {
            cout << "INSOMNIA" << '\n';
        }
    }
}