#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for ( int tc=1 ; tc<=T ; ++tc ) {
        string pancake;
        cin >> pancake;

        int res = 0;
        for ( int i=pancake.size()-1 ; i >= 0 ; --i ) {
            if ( pancake[i] == '-' ) {
                for ( int j=0 ; j<=i ; ++j ) {
                    pancake[j] = pancake[j] == '-' ? '+' : '-';
                }
                ++res;
            }
        }
        cout << "Case #" << tc << ": " << res << endl;
    }
    return 0;
}