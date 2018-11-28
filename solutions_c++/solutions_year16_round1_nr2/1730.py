/*
Will Long
Google Code Jam 2016
Round 1A - Problem 2

April 15, 2016
*/

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MAXH = 2500;
static const int MAXN = 50;

int main(int argc, const char *argv[])
{
    string fname = argv[1];
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);

    bool odd_height[MAXH + 1];
    int result[MAXN];
    int cases;
    cin >> cases;

    int N, temp;
    for (int tc = 1; tc <= cases; tc++) {
        cin >> N;
        for (int i = 1; i <= MAXH; i++) {
            odd_height[i] = false;
        }
        for (int i = 0; i < (2*N-1)*N; i++) {
            cin >> temp;
            odd_height[temp] = !(odd_height[temp]);
        }
        int pos = 0;
        for (int i = 1; i <= MAXH; i++) {
            if (odd_height[i]) {
                result[pos++] = i;
            }
        }
        cout << "Case #" << tc << ":";
        vector<int> result_vector(result, result+N);
        sort (result_vector.begin(), result_vector.end()); 
        for (vector<int>::iterator it = result_vector.begin(); it!=result_vector.end(); ++it) {
            cout << ' ' << *it;
        }
        cout << '\n';
    }

    return 0;
}