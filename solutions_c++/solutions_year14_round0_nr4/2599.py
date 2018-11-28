#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

const double EPS = 1e-7;

int war(vector<double> v1, vector<double> v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    
    int j = 0;
    int result = 0;
    for (int i = 0; i < v2.size(); ++i) {
        if (v2[i] + EPS > v1[j]) {
            ++result;
            ++j;
        }
    }
    
    return static_cast<int>(v1.size()) - result;
}

int dwar(vector<double> v1, vector<double> v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    
    int result = 0;
    int j = 0;
    for (int i = 0; i < v1.size(); ++i) {
        if (v1[i]  < v2[j] + EPS) {
            ++result;
        } else {
            ++j;
        }
    }
    
    return static_cast<int>(v1.size()) - result;
}

void solve() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N;
        cin >> N;
        
        vector<double> v1(N, 0);
        for (int i =0; i < N; ++i) {
            double current;
            cin >> current;
            v1[i] = current;
        }
        
        vector<double> v2(N, 0);
        for (int i =0; i < N; ++i) {
            double current;
            cin >> current;
            v2[i] = current;
        }
        
        printf("Case #%d: %d %d\n", t, dwar(v1, v2), war(v1, v2));
    }
}

int main(int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    solve();
    return 0;
}

