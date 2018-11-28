#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int war(vector<double>& vec1, vector<double>& vec2) {
    int pos1 = 0, pos2 = 0;
    int score = 0;

    while (pos1 < vec1.size() && pos2 < vec2.size()) {
        if (vec2[pos2] > vec1[pos1]) {
            score++;
            pos1++;
            pos2++;
        }
        else {
            pos2++;
        }
    }

    return vec2.size() - score;
}

int deceitful_war(vector<double>& vec1, vector<double>& vec2) {
    set<double> set(vec2.begin(), vec2.end());
    int score = 0;

    for (int i = 0; i < vec1.size(); i++) {
        if (vec1[i] < *(set.begin())) {
            set.erase(*(set.rbegin()));
        }
        else {
            auto itlow = set.lower_bound(vec1[i]);
            --itlow;
            set.erase(itlow);
            score++;
        }
    }

    return score;
}

int main() {
    int T, n;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> n;
        vector<double> vec1, vec2;
        double data;

        for (int i = 0; i < n; i++) {
            cin >> data;
            vec1.push_back(data);
        }
        for (int i = 0; i < n; i++) {
            cin >> data;
            vec2.push_back(data);
        }

        sort(vec1.begin(), vec1.end());
        sort(vec2.begin(), vec2.end());

        cout << "Case #" << t << ": " << deceitful_war(vec1, vec2) << " " << war(vec1, vec2) << endl;
    }
}
