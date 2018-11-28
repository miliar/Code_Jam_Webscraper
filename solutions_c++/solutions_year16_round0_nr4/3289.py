#include <iostream>
#include <string>
#include <queue>

using namespace std;

void solve(){
    int K;
    int C;
    int S;
    cin >> K >> C >> S;
    for(int i = 1; i <= K; i++){
        cout << i;
        if(i != K){
            cout << " ";
        }
    }
    cout << endl;


}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
