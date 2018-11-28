#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool heap_valid(const vector<pair<int, char>>& h, int count) {
    if (count == 0)
        return true;
    bool ret = h.front().first * 2 <= count;
    return ret;
}

string solve(const vector<int>& V) {
    string ret = "";
    vector<pair<int, char>> P;
    int count = 0;
    for (int i = 0; i < V.size(); i++) {
        P.emplace_back(make_pair(V[i], i + 'A'));
        count += V[i];
    }

    make_heap(P.begin(), P.end());

    while (count) {
        pop_heap(P.begin(), P.end());
        auto largest = P.back(); P.pop_back();
        ret += largest.second;
        count -= 1;
        if (count == 0)
            break;
        if (largest.first > 1 ) {
            P.push_back(make_pair(largest.first - 1, largest.second));
            push_heap(P.begin(), P.end());
        }

        auto P_backup = P;

        pop_heap(P.begin(), P.end());
        auto candidate = P.back(); P.pop_back();
        if (candidate.first > 1 ) {
            P.push_back(make_pair(candidate.first - 1, candidate.second));
            push_heap(P.begin(), P.end());
        }

        if (heap_valid(P, count - 1)) {
            ret += candidate.second;
            count -= 1;
        }
        else {
            P = P_backup;
        }
        if (count) {
            ret += ' ';
        }
    }

    return ret;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<int> V;
        while (N--) {
            int v;
            cin >> v;
            V.push_back(v);
        }
        auto s = solve(V);
        cout << "Case #" << t << ": " << s << endl;
    }
    return 0;
}