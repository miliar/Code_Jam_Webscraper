#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;

    int n;
    int stood = 0;
    int need = 0;
    string shy;
    for(int j = 1; j <= t; ++j) {
        stood = need = 0;
        cin >> n;
        cin >> shy;

        stood = shy[0] - '0';
        for(int i = 1; i <= n; ++i) {
            if(stood < i && shy[i] > '0') {
                need = need +  i - stood;
                stood = stood + need;
            }
            stood = stood + shy[i] - '0';
            // cout << "Stood: " << stood << " Need: " << need << endl;
        }

        cout << "Case #" << j << ": " << need << endl;
    }

    return 0;
}