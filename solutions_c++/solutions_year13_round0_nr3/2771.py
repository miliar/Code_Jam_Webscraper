#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <math.h>
#include <string.h>
#include <stack>
#include <string>

using namespace std;

string intToStr(int n) {
    if(n == 0) return "0";
    string ans = "";
    while(n > 0) {
        ans = (char) ((n % 10) + '0') + ans;
        n /= 10;
    }
    return ans;
}

int strToInt(string n) {
    int ans = 0;
    for(int i = 0; i < n.size(); i++){
        ans += (n[n.size() -i - 1] - '0') * pow(10, i);
    }
    return ans;
}

int n, a, b;
bool isPal[1000*1000+1];

bool isPalindrome(unsigned long long n){
    unsigned long long s = 0, a = n;
    while(n > 0){
        unsigned long long rem = n % 10;
        s = s * 10 + rem;
        n /=10;
    }
    return s == a;
}

void fillPal(){
    for(unsigned long long i = 0; i <= 1000000; i++){
        isPal[i] = isPalindrome(i);
    }
}

int main(void){
    fillPal();
    int test = 1;
    freopen("in.in.c", "r", stdin);
    freopen("out.out", "w", stdout);
    cin >> n;
    for(int o = 0; o < n; o++){
        cin >> a >> b;
        int ans = 0;
        for(int i = a; i <= b; i++){
            int sq = (int) sqrt(i);
            if(isPal[i] && (sq * sq == i) && isPal[sq]) {
                ans++;
            }
        }
        cout << "Case #" << test++ << ": " << ans << endl;
    }
    return 0;
}
