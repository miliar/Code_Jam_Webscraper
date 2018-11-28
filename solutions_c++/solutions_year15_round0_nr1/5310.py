//#include<bits/stdc++.h>
#include<iostream>
#include<math.h>
#include<set>

using namespace std;

int nTest, Smax, cases;
string s;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> nTest;

    while(nTest--) {
        cin >> Smax >> s;
        int current = s[0] - '0', ans = 0;
        for(int i = 1; i < s.size(); i++)
            if(current >= i) current += s[i] - '0';
            else ans += i - current, current += i - current, i--;
        cout << "Case #" << ++cases << ": " << ans << "\n";
    }
}
