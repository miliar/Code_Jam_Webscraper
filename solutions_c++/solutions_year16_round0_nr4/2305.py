#include <iostream>

using namespace std;

int main()
{
    int T, K, C, S;
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> K >> C >> S;
        cout << "Case #" <<i << ":";
        for(int j = 1; j <= K; j++){
            cout <<" " << j;
        }
        cout << endl;
    }
    return 0;
}
