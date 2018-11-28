#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <sstream>
using namespace std;
typedef vector<int> VI;
#define REP( i, m, n ) for ( int i = (int)( m ); i < (int)( n ); ++i )

bool isPalindrome(int n) {
    bool ret = true;

    stringstream ss;
    ss << n;
    string str = ss.str();
    
    REP(i, 0, str.size()/2) {
        if (str[i] != str[str.size()-1-i]) {
            ret = false;
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    
    int T;
    cin >> T;

    VI answers;

    REP(i, 0, T) {
        int a, b;
        cin >> a >> b;

        bool palindrome = false;
        bool square = false;
        int ans = 0;
        
        REP(j, a, b+1) {
            palindrome = false;
            square = false;
            if (isPalindrome(j)) {
                palindrome = true;
            }
            REP(k, 1, b) {
                if (k*k > j)    break;
                if (k*k == j) {
                    if (isPalindrome(k))    square = true;
                }   
            }
            
            if (palindrome && square) {
                ++ans;
            };
        }
        answers.push_back(ans);
    }

    int i = 1;
    for (auto ans : answers) {
        cout << "Case #" << i << ": " << ans << endl;
        ++i;
    }
}
