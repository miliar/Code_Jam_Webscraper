#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <list>
#include <set>
#include <map>

#define lout(x) cout<<x<<endl
#define out(x)  cout<<x
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)

typedef long long ll;

using namespace std;

int main() {
    ll T, N, M, A, B;
    ll i, j, k;
    std::vector<ll> S;

    cin >> T;
    for1(i, T) {
        cout << "Case #" << i << ": ";
        cin >> N;

        forn(j, N) {
            cin >> A;
            S.push_back(A);
        }
        
        while(count(S.begin(), S.end(), 1) != 3) {

            std::vector<ll>::iterator it = max_element(S.begin(), S.end());
            if(*it == 0) {
                break;
            } else {
                out((char)(it - S.begin() + 'A'));
                *it = *it - 1;
            }

            if(count(S.begin(), S.end(), 1) == 3)
                break;

            it = max_element(S.begin(), S.end());
            if(*it == 0) {
                break;
            } else {
                out((char)(it -S.begin() + 'A') << " ");
                *it = *it - 1;
            }
        }

        if(count(S.begin(), S.end(), 1) == 3) {
            std::vector<ll>::iterator it = max_element(S.begin(), S.end());
            
            out((char)(it -S.begin() + 'A') << " ");
            *it = *it-1;

            it = max_element(S.begin(), S.end());
            out((char)(it - S.begin() + 'A'));
            *it = *it - 1;

            it = max_element(S.begin(), S.end());
            out((char)(it - S.begin() + 'A'));
            *it = *it - 1;
        }

        cout << endl;
        S.resize(0);
    }

    return 0;
}