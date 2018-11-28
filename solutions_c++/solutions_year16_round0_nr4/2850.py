#include <iostream>

using namespace std;

int main()
{
    int K, C, S, n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> K >> C >> S;
        cout << "Case #" << i << ":";
        for (int j = 1; j <= K; j++) {
            cout << " " << j;
        }
        cout << endl;

    }
    return 0;
}

