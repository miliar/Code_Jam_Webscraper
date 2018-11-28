#include <iostream>
#include <cmath>

#define ULL unsigned long long

using namespace std;

int T, tcase;
int K, C, S;

int main()
{
    int pos;
    cin >> T;
    tcase = 1;
    while (tcase<=T) {
        cin >> K >> C >> S;

        pos = K;

        cout << "Case #" << tcase++ << ":";
        for (int i=1; i<=pos; ++i) {
            cout << " " << i;
        }
        cout << endl; 
    }
}
