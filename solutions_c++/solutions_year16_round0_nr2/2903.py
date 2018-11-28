#include<iostream>
#include<string>
using namespace std;

int main() {

    int T = 0;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string pan;
        cin >> pan;

        int revs = 0;
        int index = pan.size() - 1;
        char cur = '+'; 
        while(index >= 0){
            if (pan[index] != cur){
                cur = pan[index];
                revs++;
            }
            index--;
        }
        int ans = revs;
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }

    return 0;
}