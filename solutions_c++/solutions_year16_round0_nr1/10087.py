#include <iostream>
#include <vector>
using namespace std;

bool find(vector<bool>& numbers){
    for (int i = 0; i < 10; ++i) {
        if (!numbers[i]) return false;
    }
    return true;
}


bool calculate(long long x_orig, vector<bool>& numbers) {
    int x = x_orig;
    while (x) {
        numbers[x%10] = true;
        x = x/10;
        if (find(numbers)) return x_orig;
    }
    return false;
}


int main() {
    int n;
    long long x;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        vector<bool>numbers(10, false);
        cin >> x;
        if (!x) cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        else {
            for (long long j = 1; true; ++j) {
                if (calculate(x*j, numbers)) {
                    cout << "Case #" << i+1 << ": " << x*j << endl;
                    break;
                }
            }
        }
    }
}
