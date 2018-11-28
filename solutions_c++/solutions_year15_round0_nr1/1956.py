#include <iostream>

using namespace std;

int main() {
    std::ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for( int CASE = 1; CASE <= T; CASE++ ) {
        int S_max, n = 0, needed = 0;
        cin >> S_max;

        while(cin.peek() == ' ')cin.get();
        for( int i = 0; i <= S_max; i++ ) {
            if( n < i ) {
                n = i; 
                needed++;
            }
            int m = cin.get() - '0';
            n += m;
        }
        cout << "Case #" << CASE << ": " << needed << endl;
    }

    return 0;
}
