#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
        string str;
        cin >> str;

        int cnt = 0;
        for (int i = 0; i < (int) str.size() - 1; i++)
            cnt += (str[i] != str[i + 1]);
        cnt += (str.back() == '-');

        cout << "Case #" << tnum + 1 << ": " << cnt << endl;
    }

    return 0;
}