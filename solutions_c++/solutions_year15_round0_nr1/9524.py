#include<iostream>
#include<string>
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int S;
        cin >> S;
        string in;
        cin >> in;
        int au[S+1];
        for (int j = 0; j < S+1; j++) {
            au[j] = in[j] - (int)48;
        }
        int ans = 0;
        int current = au[0];
        for (int j = 1; j < S+1; j++) {
            if (current < j && au[j] > 0) {
                ans += j-current;
                current += j-current;
            }
            current += au[j];
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
