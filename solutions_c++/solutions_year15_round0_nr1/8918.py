#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main(){
    int T, Smax;
    string s;
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> Smax >> s;
        int have = s[0] - '0', ans = 0;
        for(int j = 1; j <= Smax; j++){
            ans += max(0, j - have);
            have += (s[j] - '0') + max(0, j - have);
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
