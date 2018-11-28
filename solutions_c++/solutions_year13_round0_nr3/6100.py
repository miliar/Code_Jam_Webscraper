#include <iostream>
#include <cmath>

using namespace std;

int is_palindrome(int x) {
    int copy = x, rem, rev = 0;
    
    while(copy > 0) {
        rem = copy % 10;
        rev = rev * 10 + rem;
        copy = copy / 10;
    }
    
    if(rev == x) {
        return 1;
    } else {
        return 0;
    }
}

int is_square_of_palindrome(int x) {
    int val, palindrome;
    
    val = sqrt(x);
    
    if(val * val == x) {
        palindrome = is_palindrome(val);
        
        if(palindrome == 1) {
            return 1;
        } else {
            return 0;
        }
    } else {
        return 0;
    }
}

int find_result(int lb, int ub) {
    int i, palindrome, square, count = 0;

    for(i = lb; i <= ub; i++) {
        palindrome = is_palindrome(i);
        
        if(palindrome == 1) {
            square = is_square_of_palindrome(i);
            
            if(square == 1) {
                count++;
            }
        }
    }
    
    return count;
}

int main() {
    int i, n, *res, lb, ub;
    
    cin >> n;
    
    res = new int[n];
    
    for(i = 0; i < n; i++) {
        cin >> lb;
        cin >> ub;
        
        res[i] = find_result(lb, ub);
    }
    
    for(i = 0; i < n; i++) {
        cout << "Case #" << i+1 << ": " << res[i] << "\n";
    }
    
    return 0;
}
