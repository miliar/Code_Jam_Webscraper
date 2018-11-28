#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<functional>

using namespace std;

int time(vector<int> &v) {
    sort(v.begin(), v.end(), greater<int>());
    int res = 10001;
    for (int i = 0; i <= v.size(); i++) {
        for (int hlimit = 1; hlimit <= v[0]; hlimit++) {
            int nmove = 0;
            int maxh = 0;
            for (int j = 0; j < i; j++) {
                nmove += v[j] / hlimit;
                int highest = (v[j] - 1) / (v[j] / hlimit + 1) +1;
                if (highest > maxh)
                    maxh = highest;
            }
            if (i < v.size() && v[i] > maxh)
                maxh = v[i];
            int total = maxh + nmove;
            if (total < res)
                res = total;
        }
    }

    return res;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int n;
        cin >> n;
        vector<int> v(n);
        for (auto &e : v)
            cin >> e;

        cout << "Case #" << i << ": " << time(v) << endl;
    }


    return 0;
}

