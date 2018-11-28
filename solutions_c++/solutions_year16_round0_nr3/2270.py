#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

string rev(string str) {
    string ret = "";
    int len = str.length();
    for(int i = 0; i < len; i++)
        ret = ret + str[len-i-1];
    return ret;
}

string convtobin(int N) {
    int ans = 0;
    while(N > 0) {
        ans += pow(10, (int)log2(N));
        N -= pow(2, (int) log2(N));
    }
    string lead = "";
    string var = to_string(ans);
    for(int i = 0; i < 15-var.length(); i++)
        lead = lead + "0";
    string str1 = lead + var;
    string str2 = rev(str1);
    return str1+str2;
}

int main() {
    freopen("jamcoin.in", "r", stdin);
    freopen("jamcoin.out", "w", stdout);
    int K, N, J;

    cout << "Case #1: " << endl;
    cin >> K >> N >> J;
    for(int i = 0; i < 500; i++) {
        cout << "1" << convtobin(i) << "1";
        for(int i = 2; i <= 10; i++) {
            cout << " " << (i+1);
        }
        cout << endl;
    }

}
