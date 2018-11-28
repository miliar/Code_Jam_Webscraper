#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef long long ll;

const int ALL_FOUND = pow(2,10)-1;

class A {

private:
    ll N;

public:
    void init() {
        cin >> N;
    }
    
    void solution(int x) {

        cout << "Case #" << x << ": ";

        if ( N == 0 ) {
            cout << "INSOMNIA";
        }
        else {
            unsigned int found = 0;
            ll i;
            for ( i = 1; ; ++i ) {
                ll Ni = N * i;
                while ( Ni > 0 ) {
                    found |= ( 1 << (Ni%10) );
                    Ni /= 10;
                }
                if ( found == ALL_FOUND )
                    break;
            }
            cout << N*i;
        }
        cout << endl;
    }

};

int main() {
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> T;

    for ( int i = 1; i <= T; ++i ) {
        A sol;
        sol.init();
        sol.solution(i);
    }
}
