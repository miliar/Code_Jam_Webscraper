#include <iostream>
using namespace std;

int main(){
    long T;
    string S;

    cin >> T;
    for (int i = 1; i <= T; i++){
        cin >> S;
        cout << "Case #" << i << ": " ;

        int ans = 0;
        int len = S.size();
        S = S + "+";

        for (int j = 0; j < len; j++){
            if (S[j] != S[j+1]){
                ans++;
            }
        }

        cout << ans << endl;

    }
}
