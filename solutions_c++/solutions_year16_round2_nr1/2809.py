#include "iostream"
#include "vector"
#include "map"
#include "queue"
#include "stack"
#include "algorithm"
#include "cstdio"
#include "string"

using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vll;
typedef queue<ll> qll;
typedef stack<ll> sll;
typedef map<ll, ll> mll;
typedef pair<ll, ll> pll;


void solve() {
    ui T;
    string str;

    ll digits[10];

    scanf("%u\n", &T);
    for (ull t = 1; t <= T; ++t)
    {
        for (int i = 0; i < 10; ++i)
        {
            digits[i] = 0;
        }
        getline(cin, str);
        for (int i = 0; i < str.length(); ++i)
        {
            digits[0] += (str[i] == 'Z') ? 1 : 0;
            digits[1] -= (str[i] == 'Z') ? 1 : 0;

            digits[2] += (str[i] == 'W') ? 1 : 0;
            digits[1] -= (str[i] == 'W') ? 1 : 0;
            digits[3] -= (str[i] == 'W') ? 1 : 0;

            digits[4] += (str[i] == 'U') ? 1 : 0;
            digits[1] -= (str[i] == 'U') ? 1 : 0;
            digits[5] -= (str[i] == 'U') ? 1 : 0;
            digits[9] += (str[i] == 'U') ? 1 : 0;

            digits[6] += (str[i] == 'X') ? 1 : 0;
            digits[9] -= (str[i] == 'X') ? 1 : 0;
            digits[7] -= (str[i] == 'X') ? 1 : 0;

            digits[8] += (str[i] == 'G') ? 1 : 0;
            digits[9] -= (str[i] == 'G') ? 1 : 0;
            digits[3] -= (str[i] == 'G') ? 1 : 0;

            // save
            digits[3] += (str[i] == 'T') ? 1 : 0;

            digits[1] += (str[i] == 'O') ? 1 : 0;

            digits[5] += (str[i] == 'F') ? 1 : 0;
            digits[9] -= (str[i] == 'F') ? 1 : 0;

            digits[7] += (str[i] == 'S') ? 1 : 0;

            digits[9] += (str[i] == 'I') ? 1 : 0;
        }

        cout << "Case #" << t << ": ";
        for (int i = 0; i < 10; ++i)
        {
            while(digits[i]-- > 0) {
                cout << i;
            }
        }
        cout << endl;
    }


}

int main(int argc, char const *argv[]) {
    solve();
}

