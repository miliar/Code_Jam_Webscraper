#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int T; cin >> T;
    for(int _t = 0; _t < T; _t++) {
        int N; string s;
        cin >> N >> s;
        int needed = 0;
        int clapping = 0;
        for(int i = 0; i <= N; i++) {
            int Si = s[i] - '0';
            if(clapping < i){
                needed += i - clapping;
                clapping += i - clapping;
            }
            clapping += Si;

        }

        printf("Case #%d: %d\n", _t + 1, needed);
    }
}
