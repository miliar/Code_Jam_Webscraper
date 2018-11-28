#include <fstream>
#include <string>
#define MAXLEN 1000
using namespace std;

string s;
bool biti[MAXLEN + 1];

int main () {
    ifstream cin("A.in");
    ofstream cout("A.out");

    int T;
    cin >> T;
    for (int tst = 1 ; tst <= T ; ++tst) {
        int k;
        cin >> s >> k;
        int n = s.size();
        for (int i = 0 ; i < n ; ++i)
            biti[i] = (s[i] == '+' ? 0 : 1);

        int flips = 0;
        for (int i = 0 ; i <= (n - k) ; ++i)
            if (biti[i]) {
                ++flips;
                for (int j = i ; j < i + k ; ++j)
                    biti[j] ^= 1;
            }

        bool happy = true;
        for (int i = 0 ; i < n && happy ; ++i)
            if (biti[i])
                happy = false;

        cout << "Case #" << tst << ": ";
        if (happy)
            cout << flips << "\n";
        else
            cout << "IMPOSSIBLE\n";
    }

    return 0;
}
