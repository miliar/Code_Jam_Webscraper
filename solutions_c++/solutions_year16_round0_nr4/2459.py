#include <iostream>
using namespace std;

// original K tiles
// C times multipled
// S workers
void solve(int K, int C, int S)
{
}

int main(void)
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        int K, C, S;
        cin >> K;
        cin >> C;
        cin >> S;
        solve(K, C, S);
        cout << "Case #" << i << ":";
        for(int j = 1; j <= S; ++j) 
            cout << " " << j;
        cout << endl;
    }
}

