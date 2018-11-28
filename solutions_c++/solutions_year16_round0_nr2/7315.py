#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int CASE = 1; CASE <= T; CASE++){
        cout << "Case #" << CASE <<": ";
        string str;
        cin >> str;
        int N = (int)str.size();
        
        char lastpc = '+';
        int res = 0;
        for(int i = N-1; i >= 0; i--){
            if (str[i] != lastpc){
                lastpc = str[i];
                res++;
            }
        }
        
        cout << res << endl;
    }
    return 0;
}
