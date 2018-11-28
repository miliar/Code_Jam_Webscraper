#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

vector<int> s(1002);

int main() {
    int t; cin >> t;
    for(int tcase = 1; tcase <= t; ++tcase) {
        int count = 0;
        int invite = 0;

        int smax; cin >> smax;
        for(int i = 0; i < smax+1; ++i) {
            char temp; cin >> temp;
            s[i] = temp - '0';
            if(count < i && s[i] > 0) {
                invite += i-count;
                count = i;
            }

            count += s[i];
        }

        printf("Case #%i: %i\n", tcase, invite);
    }

    return 0;
}
