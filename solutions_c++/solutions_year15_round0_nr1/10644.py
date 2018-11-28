#include <iostream>
#include <string>

using namespace std;

int main(){
    int N = 0;
    cin >> N;
    cin.ignore(10,'\n');
    for (int i = 0; i < N; ++i){
        int max;
        string s;
        cin >> max >> s;
        int totalAvailable = 0;
        int needed = 0;
        for (int j = 0; j <= max; ++j){
            int val = s[j] - '0';
            if (totalAvailable < j && val != 0){
                needed += j - totalAvailable;
                totalAvailable += needed;
            }
            totalAvailable += val;
        }

        cout << "Case #" << i+1 << ": " << needed << endl;
    }

    return 0;
}
