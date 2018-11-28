#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int smax;
        cin >> smax;
        vector<int> shyness(smax + 1);
        for(int i = 0; i <= smax; i++) {
            char c;
            cin >> c;
            shyness[i] = c - '0';
        }
        int count = 0;
        int add = 0;
        for(int i = 0; i <= smax; i++) {
            if(count < i) {
                add += i - count;
                count = i;
            }
            count += shyness[i];
        }
        cout << "Case #" << t + 1 << ": " <<  add << endl;
    }
    return 0;
}
