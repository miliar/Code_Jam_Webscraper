#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <iomanip>
#include <ctime>
#include <cmath>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

const long long INF = 1000000000000000001ll;
const int INFint = (1<<28);
const int MOD = 1000000007;
const long double EPS = 1e-8;

bool comp(int x, int y){
    return (x > y);
}

pair<int, char> m[255][255];

pair<int, char> mul(pair<int, char> tu, char l) {
    int c = m[tu.second][l].first;
    char s = m[tu.second][l].second;


    return mp(tu.first * c, s);
}
int main(){
    ios_base::sync_with_stdio(0);
//    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;


    m['1']['1'] = mp(1, '1');
    m['1']['i'] = mp(1, 'i');
    m['1']['j'] = mp(1, 'j');
    m['1']['k'] = mp(1, 'k');

    m['i']['1'] = mp(1, 'i');
    m['i']['i'] = mp(-1, '1');
    m['i']['j'] = mp(1, 'k');
    m['i']['k'] = mp(-1, 'j');

    m['j']['1'] = mp(1, 'j');
    m['j']['i'] = mp(-1, 'k');
    m['j']['j'] = mp(-1, '1');
    m['j']['k'] = mp(1, 'i');

    m['k']['1'] = mp(1, 'k');
    m['k']['i'] = mp(1, 'j');
    m['k']['j'] = mp(-1, 'i');
    m['k']['k'] = mp(-1, '1');
//    pair<int, char> c = mul(mp(1, 'j'), 'k');
//    cout << c.first << ' ' << c.second << endl;
//    return 0;

    for(int t = 1; t<= T; t++) {
        int n, x;
        cin >> n >> x;
        string s;
        cin >> s;
        int i = 0;
        pair<int, char> c = make_pair(1, '1');
        while (i < 4 * n) {
            c = mul(c, s[i % n]);
            i++;
//            cout << c.first << ' ' << c.second << endl;

            if (c.first == 1 && c.second == 'i')
                break;
        }
        if (4 * n == i) {
            cout << "Case #" << t << ": " << "NO" << endl;
            continue;
        }

        c = make_pair(1, '1');
        while (i < 8 * n) {
            c = mul(c, s[i % n]);
            i++;
            if (c.first == 1 && c.second == 'j')
                break;
        }
        if (8 * n == i) {
            cout << "Case #" << t << ": " << "NO" << endl;
            continue;
        }


        c = make_pair(1, '1');
        while (i < 12 * n) {
            c = mul(c, s[i % n]);
            i++;
            if (c.first == 1 && c.second == 'k')
                break;
        }
        if (12 * n == i) {
            cout << "Case #" << t << ": " << "NO" << endl;
            continue;
        } else {
            if (x <= (i - 1) / n) {
                cout << "Case #" << t << ": " << "NO" << endl;
                continue;
            }
        }
        c = make_pair(1, '1');
        int pv = (x - 1 - (i - 1) / n) % 4;
        while (i % n != 0) {
            c = mul(c, s[i % n]);
            i++;
        }
        for (int j = 0; j < pv * n; j++) {
            c = mul(c, s[i % n]);
            i++;
        }
        if (c.first == 1 && c.second == '1') {
            cout << "Case #" << t << ": " << "YES"<< endl;
        } else {
            cout << "Case #" << t << ": " << "NO"<< endl;
        }
    }

    return 0;
}
