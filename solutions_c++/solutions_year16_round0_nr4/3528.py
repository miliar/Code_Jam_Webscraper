#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef long long ll;

const string IMP = "IMPOSSIBLE";

class D {

private:
    int K, C, S;

public:
    void init() {
        cin >> K >> C >> S;
    }
    
    void solution(int x) {
        cout << "Case #" << x << ": ";

        int minS;
        if ( C <= K )
            minS = K-C+1;
        else
            minS = 1;

        if ( S < minS ) {
            cout << IMP;
        }
        else {
            ll idx = find_index(C);
            for ( int i = 1; i <= minS; ++i ) {
                cout << idx--;
                if ( i < minS ) cout << " ";
            }
        }

        cout << endl;
    }

    ll find_index(int c) {
        ll ret;
        int s = K-c+1;

        if ( c == 1 )
            ret = K;
        else if ( c <= K )
            ret = (ll)K * ( find_index(c-1) - (ll)s );
        else
            ret = find_index(K);

        return ret;
    }
};

int main() {
    int T;

    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);

    cin >> T;

    for ( int i = 1; i <= T; ++i ) {
        D sol;
        sol.init();
        sol.solution(i);
    }
}
