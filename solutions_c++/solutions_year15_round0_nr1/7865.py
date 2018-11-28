//
// Problem A. Standing Ovation
//

#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void solve(int t){
    int l;
    string s;
    cin >> l >> s;
    
    int sum = 0;
    int add = 0;
    for (int i = 0; i <= l; i++) {
        if (sum < i) {
            add += i-sum;
            sum = i;
        }
        sum += s[i]-'0';
    }
    
    printf("Case #%d: %d\n", t, add);
}

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
