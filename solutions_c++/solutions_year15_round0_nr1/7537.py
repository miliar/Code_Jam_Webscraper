#include <stdio.h>
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    int t = 0;
    while(true) {
        if(++t > T) break;
        int maxlevel;
        string digits;
        cin >> maxlevel >> digits;


        int has_stand = 0;
        int add = 0;
        for(int i = 0; i < digits.size(); ++i){
            if(i > has_stand){
                add += i - has_stand;
                has_stand += i - has_stand;
            }
            has_stand += digits[i] - '0';
        }
        cout << "Case #" << t << ": " << add << endl;
    }
    return 0;
}
