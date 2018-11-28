#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef double db;
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <string, string> pss;
typedef vector <int> lint;
typedef double db;
string solve() {
    int f, s, msf = 0, mss = 0;
    cin >> f;
    --f;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int x;
            cin >> x;
            if (i == f) msf |= 1<<(x-1);
        }
    cin >> s;
    --s;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int x;
            cin >> x;
            if (i == s) mss |= 1<<(x-1);
        }
    msf &= mss;
    if (msf == 0)
        return "Volunteer cheated!";
    int cnt = 0, id = 0;
    for (int i = 0; i < 16; ++i)
        if ((msf>>i)&1) {
            cnt++;
            id = i;
        }
    if (cnt > 1) 
        return "Bad magician!";
    char ss[10];
    sprintf(ss, "%d", id + 1);
    return string(ss); 
}
         
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    return 0;
}
