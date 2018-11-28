#include <bits/stdc++.h>

using namespace std;

const int N = 101;
vector < vector<int> > v;
int n;
int M[51][51];
int used[51];

bool test (int start) {
    int q = 0;
    int i = start;
    while (q != n) {
        for (int j = 0; j < n; ++j) {
            M[i][j] = v[i][j];
        }
        used[i] = true;
        q++;
        i += 2;
    }
    int col = 0;
    
}   

int cnt[2501];

int main (void) {
    int T;
    cin >> T;
    for (int c = 1; c <= T; ++c) {
        cout << "Case #" << c << ": ";
        cin >> n;
        int best = 0;
        memset (cnt, 0, sizeof cnt);
        for (int i = 0; i < 2*n-1; ++i) {
            for (int j = 0; j  < n; ++j) {
                int x;
                cin >> x;
                cnt[x]++;
            }
        }

        for (int i = 1; i<=2500; ++i) {
            if (cnt[i]%2 == 1) {
                cout << i << " ";
            }
        }
        cout << endl;

    }


}
