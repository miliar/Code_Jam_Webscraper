#include <bits/stdc++.h>
using namespace std;
typedef long long int lint;

string best[13][128];

void code() {
    int N;
    cin >> N;
    int R, P, S;
    cin >> R >> P >> S;

    best[0]['R'] = "R";
    best[0]['S'] = "S";
    best[0]['P'] = "P";

    for(int i = 1; i <= N; i++) {
        if(best[i-1]['R'] < best[i-1]['S']) {
            best[i]['R'] = best[i-1]['R'] + best[i-1]['S'];
        } else {
            best[i]['R'] = best[i-1]['S'] + best[i-1]['R'];
        }
        if(best[i-1]['S'] < best[i-1]['P']) {
            best[i]['S'] = best[i-1]['S'] + best[i-1]['P'];
        } else {
            best[i]['S'] = best[i-1]['P'] + best[i-1]['S'];
        }
        if(best[i-1]['P'] < best[i-1]['R']) {
            best[i]['P'] = best[i-1]['P'] + best[i-1]['R'];
        } else {
            best[i]['P'] = best[i-1]['R'] + best[i-1]['P'];
        }
        cerr << i << endl;
        cerr << best[i]['R'] << endl;
        cerr << best[i]['P'] << endl;
        cerr << best[i]['S'] << endl;
    }

    string s1 = best[N]['R'];
    string s2 = best[N]['P'];
    string s3 = best[N]['S'];
    vector<string> arr;
    arr.push_back(s1);
    arr.push_back(s2);
    arr.push_back(s3);

    sort(arr.begin(), arr.end());
    for(int i = 0; i < 3; i++) {
        cerr << arr[i] << endl;
        int r = 0, p = 0, s = 0;
        for(int j = 0; j < arr[i].size(); j++) {
            switch(arr[i][j]) {
                case 'R': r++;
                          break;
                case 'P': p++;
                          break;
                case 'S': s++;
                          break;
            }
        }
        if(r == R && p == P && s == S) {
            cout << arr[i];
            return;
        }
    }
        cout << "IMPOSSIBLE";
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int tt=1; tt<=t; tt++) {
        cout << "Case #" << tt << ": ";
        code();
        cout << endl;
    }
}
