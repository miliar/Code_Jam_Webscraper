#include <iostream>
#include <vector>
using namespace std;

int MAX = 100;

vector<int> fair_and_square;

bool is_palindrome(int n) {
    vector<int> digits;
    
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    
    int ix1 = 0, ix2 = digits.size()-1;
    
    while (ix1 < ix2) {
        if (digits[ix1] != digits[ix2]) {
            return false;
        }
       ++ix1; --ix2;
    }

    return true;
}

int main()
{
    int T, A, B, square, answ = 0, case_ = 0;
    cin >> T;
    
    for (int i = 1; i <= MAX; i++) {
        if (is_palindrome(i)) {
            square = i*i;
            if (is_palindrome(square)) {
                fair_and_square.push_back(square);
            }
        }
    }
    
    while (T--) {
        cin >> A >> B;
        ++case_;
        answ = 0;
    
        for (int i = 0; i < fair_and_square.size(); i++) {
            if (fair_and_square[i] > B) {
                break;
            }
            if (fair_and_square[i] >= A) {
                ++answ;
            }
        }
        
        cout << "Case #" << case_ << ": " << answ << endl; 
    }
    

    
    return 0;
}
