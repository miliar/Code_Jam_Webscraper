#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;

int T, B, N, i, j;

int main() {
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    
    cin >> T;
    
    for (i = 0; i < T; i++) {
        int ans1 = 0, ans2 = 0, maxDiff = 0;
        cin >> N;
        vector<int> v(N);
        cin >> v[0];
        for (j = 1; j < N; j++) {
            cin >> v[j];
            if (v[j] < v[j-1]) {
                ans1 += v[j-1] - v[j];
                maxDiff = max(maxDiff, v[j-1] - v[j]);
            }
        }
        for (j = 0; j < N-1; j++) {
            ans2 += min(maxDiff, v[j]);
        }
        cout << "Case #" << i+1 << ": " << ans1 << " " << ans2 << endl;
    }
    
    return 0;
}