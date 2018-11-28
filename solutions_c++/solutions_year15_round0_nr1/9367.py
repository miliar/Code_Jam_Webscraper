#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    for(int caseno = 0; caseno < cases; ++caseno) {
        int smax;
        char sAscii;
        vector<int> smaxes;
        int res = 0;
        cin >> smax;
        cin.get();
        for(int i = 0; i < smax + 1; ++i) {
            char c;
            cin.get(c);
            int s = (c - '0');
            smaxes.push_back(s);
        }

        int clapping = smaxes[0];
        for(int shyness = 1; shyness < smaxes.size(); ++shyness) {
            int members = smaxes[shyness];
            if(shyness > clapping) {
                res += (shyness - clapping);
                members += (shyness - clapping);
            }
            clapping += members;
        }

        printf("Case #%d: %d\n", caseno + 1, res);
    }
}