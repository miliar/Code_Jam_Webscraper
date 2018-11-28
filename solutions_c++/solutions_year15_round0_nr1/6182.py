/*
 * Created on: 2015-04-11 22:58
 * Created by: suren
 *
 * Distributed under beerware licence.
 */

#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()

int main() {
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas++) {
        int s;
        string x;
        cin >> s >> x;
        int c = (x[0] - '0');
        int req = 0;
        for(int i = 1; i <= s; i++) {
            if(c < i) {
                req += i - c;
                c = i;
            }
            c += (x[i] - '0');
        }

        printf("Case #%d: %d\n", cas, req);
    }

    return 0;
}
