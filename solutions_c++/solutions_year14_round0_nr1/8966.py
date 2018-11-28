#include <iostream>
#include <set>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <time.h>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <bitset>

//#define MYLOCAL

#pragma comment(linker, "/STACK:256000000")

using namespace std;

int main() {
#ifdef MYLOCAL
    freopen("/home/maks/input.txt", "rt", stdin);
    freopen("/home/maks/output.txt", "wt", stdout);
    clock_t beginTime = clock();
#endif

    int t,ans1,ans2, cnt = 0, temp, ans;
    set<int> st;
    cin >> t;
    for (int test = 0; test < t; test++) {
        st.clear();
        cnt = 0;
        cin >> ans1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> temp;
                if (i == ans1 - 1)
                    st.insert(temp);
               }
        }
        cin >> ans2;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> temp;
                if (i == ans2 - 1)
                    if (st.find(temp) != st.end()) {
                        cnt++;
                        ans = temp;
                    }
            }
        }
        cout << "Case #" << test + 1 << ": ";
        if (cnt == 0)
            cout << "Volunteer cheated!";
        else if (cnt == 1)
            cout << ans;
        else
            cout << "Bad magician!";
        cout << endl;
    }


#ifdef MYLOCAL
    cout << endl << "time: " << double(clock() - beginTime) / CLOCKS_PER_SEC;
#endif
    return 0;
}
