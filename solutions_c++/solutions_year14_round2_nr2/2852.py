#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <utility>

using namespace std;

int T, a, b, k;

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);

    cin >> T;
    for(int i = 1; i <= T; i++) {
        cin >> a >> b >> k;
        int cnt = 0;
        for(int ia = 0; ia < a; ia++) {
            for(int ib = 0; ib < b; ib++) {
                if( (ia & ib) < k) {
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n", i, cnt);
    }

	return 0;
}
