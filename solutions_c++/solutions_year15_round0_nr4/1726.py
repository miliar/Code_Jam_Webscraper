#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <bitset>
#include <numeric>
#include <ctime>
#include <cassert>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;
typedef long long ll;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int main() {
	int _; cin >> _; 
	for (int __ = 1; __ <= _; __ ++) {
        printf ("Case #%d: ", __);
        int X, R, C;
        cin >> X >> R >> C;
        if (R > C) swap(R, C);
        if (R * C < X || X >= 7 || C < X || (X+1)/2 > R || R * C % X != 0) {
           printf ("RICHARD\n");
           continue;
        }
        if (R >= X || R >= X/2 + 1) {
           printf ("GABRIEL\n");
           continue;
        }
        if (X == 6 || X == 5 || X == 4) {
           printf ("RICHARD\n");
           continue;
        }
        printf ("GABRIEL\n");
	}
	return 0; 
}
