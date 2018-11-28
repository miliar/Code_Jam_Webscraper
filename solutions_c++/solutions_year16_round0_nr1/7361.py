#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <utility>
#include <iomanip>
#include <bitset>
#include <fstream>
#include <limits>

using namespace std;

typedef long long int64;

int64 LastNumber(int64 N) {
    assert(N > 0);
    bitset<10> seen;

    int64 last_number;
    for (int64 i = 1; i <= 1000000000LL; i++) {
        last_number = N * i;
        int64 tmp = last_number * 10;

        while (tmp /= 10) {
            seen.set(tmp % 10);
        }

        if (seen.count() == 10)
            break;
    }

    assert(seen.count() == 10);
    return last_number;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        int64 N;
        cin >> N;
        
        cout << "Case #" << test_case << ": ";

        if (N > 0)
            cout << LastNumber(N);
        else
            cout << "INSOMNIA";
        cout << "\n";
    }

    return 0;
}
