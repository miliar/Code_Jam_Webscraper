#include <bits/stdc++.h>
#define MAXN 100002
#define INF 1000000
using namespace std;
typedef long long ll;
typedef int char_32;
#define MAXN1 100002
#define INF2 1000000
#define MAXN3 100002
#define INF4 1000000
#define MAXN5 100002
#define INF6 1000000
#define MAXN7 100002
#define INF8 1000000
#define MAXN9 100002
#define INF10 1000000
#define MAXN11 100002
#define INF12 1000000
#define MAXN13 100002
#define INF14 1000000
#define MAXN15 100002
#define INF16 1000000

map <string, int> Mplus, Mminus;

int f(string s, int znach) {

    for(int i = s.length() - 1; i >= 0; --i) {
        if(znach == 1) {

            if(s[i] == '-') {
                return f(s.substr(0, i + 1), (znach == 1 ? 0 : 1)) + 1;
            }

        }
        else {

            if(s[i] == '+') {
                return f(s.substr(0, i + 1), (znach == 1 ? 0 : 1)) + 1;
            }

        }
    }

    return 0;

}

int main() {
    //srand(time(0));
    freopen("B-large.in", "r", stdin);
    freopen("condense2.out", "w", stdout);
    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
        string s; cin >> s;

        cout << "Case #" << i << ": " << f(s, 1) << endl;
    }


}
