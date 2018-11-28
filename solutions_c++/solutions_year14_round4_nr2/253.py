// CPPFLAGS=-std=gnu++11 -O3

#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <cstdlib>
#include <string>
#include <cstdint>

#define D(x) 

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
    os << "[";
    for (int i = 0; i < vec.size(); i++) {
        if (i > 0) os << ", ";
        os << vec[i];
    }
    return os << "]";
}

int main() {
    int numCases;
    cin >> numCases;

    for (int T = 1; T <= numCases; T++) {
        int N;
        cin >> N;

        vector<int> A(N);
        vector<pair<int, int>> pairs(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
            pairs[i].first = A[i];
            pairs[i].second = i;
        }
        
        sort(pairs.begin(), pairs.end());

        vector<vector<int>> table(N+1, vector<int>(N+1, 1000000));

        table[0][0] = 0;
        for (int sum = 0; sum < N; sum++) {
            int index = pairs[sum].second;
            int left=0, right=0;
            for (int i = sum+1; i < N; i++) {
                if (pairs[i].second < index) {
                    left++;
                } else {
                    right++;
                }
            }

            for (int a = 0; a <= sum; a++) {
                int b = sum-a;
                D(cerr << "table[" << a << "][" << b << "]=" << table[a][b] << endl);
                table[a+1][b] = min(table[a+1][b], table[a][b] + left);
                table[a][b+1] = min(table[a][b+1], table[a][b] + right);
            }
        }

        int result = 1000000;
        for (int a = 0; a <= N; a++) {
            result = min(result, table[a][N-a]);
        }

        cout << "Case #" << T << ": ";
        cout << result;
        cout << endl;
    }
}
