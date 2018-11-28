#include<iostream>
#include<string>
#include<vector>

using namespace std;

int nFr(int k, string &s) {
    int max = 0;
    vector<int> v, stat;
    for (auto e : s)
        v.push_back(e - '0');

    int total = 0;
    for (int i = 0; i <= k; i++) {
        total += v[i];
        stat.push_back(total);
    }

    for (int i = 1; i <= k; i++) {
        if (v[i] && stat[i-1] < i) {
            int tmp = i - stat[i-1];
            if (tmp > max)
                max = tmp;
        }
    }

    return max;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int k;
        string s;
        cin >> k >> s;
        cout << "Case #" << i<< ": " << nFr(k, s) << endl;
    }

    return 0;
}

