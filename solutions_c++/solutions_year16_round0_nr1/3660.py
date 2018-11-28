#include <iostream>
#include <set>

using namespace std;

void addDigitsToSet(int num, set<int>& digits) {
    while(num > 0) {
        digits.insert(num%10);
        num /= 10;
    }
}

int main() {
    int T;
    unsigned long long N, Ncopy;
    cin >> T;
    for(int i=0; i<T; i++) {
        cin >> N;
        if(N == 0) {
            cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
            continue;
        }

        set<int> digits;
        addDigitsToSet(N, digits);
        
        Ncopy = N;
        while(digits.size() != 10) {
            Ncopy += N;
            addDigitsToSet(Ncopy, digits);
        }


        cout << "Case #" << (i+1) << ": " << Ncopy << endl;
    }
}
