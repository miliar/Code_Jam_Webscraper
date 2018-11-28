#include <stdint.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main()
{
    int hash[10];
    int T, N;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        // only case to INSOMNIA
        if (N == 0) { cout << "Case #" << i << ": INSOMNIA" << endl; continue; }
        memset(hash, 0, 10 * sizeof(int));
        int hash_count = 0;
        int tmp, tmp2 = N;
        while (true) {
            tmp = tmp2;
            while (tmp) {
                int mod = tmp % 10;
                tmp /= 10;

                if (hash[mod] == 0) {
                    hash[mod] = 1; ++hash_count;
                    if (hash_count == 10) break;
                }
            }
            if (hash_count == 10) break;
            tmp2 += N;
        }
        cout << "Case #" << i << ": " << tmp2 << endl;
    }
    return 0;
}