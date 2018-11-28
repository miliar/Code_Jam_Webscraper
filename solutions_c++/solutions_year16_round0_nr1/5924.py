#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <sstream>
#include <cmath>
#include <assert.h>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <algorithm>

using namespace std;

typedef long long ll;

int main() {
    string file_path = "C:\\Users\\Aidan\\Desktop\\jam\\input.in";
    ifstream data (file_path.c_str(), ios::in);
    ofstream ret ("C:\\Users\\Aidan\\Desktop\\jam\\output.out");

    int T;
    ll N;
    unordered_set<ll> dict;
    data >> T;

    for (int round = 1; round <= T; round++) {
        bool found = false;
        data >> N;
        dict.clear();

        if (N == 0) {
            ret << "Case #" << round << ": " << "INSOMNIA" << endl;
            continue;
        }
        // loop through N, 2N, 3N....till LLONG_MAX
        for (ll i = 1; i <= LLONG_MAX / N; i++) {
            ll temp = N * i;

            while(temp > 0) {
                int digit = temp % 10;
                dict.insert(digit);
                temp /= 10;
            }

            if (dict.size() == 10) {
                ret << "Case #" << round << ": " << N * i << endl;
                found = true;
                break;
            }
        }

        if (!found) {
            ret << "Case #" << round << ": " << "INSOMNIA" << endl;
        }
    }
    ret.close();
    return 0;
}
