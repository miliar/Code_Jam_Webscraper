#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<int> v;
    vector<string> best(8, "");
    vector<string> worst(8, "");
    vector<string> cur(8, "");
    vector<string> clean(8, "");

    int j = 0;

    for (int i = 0; i < 8; ++i)
        v.push_back(i);

    while (next_permutation(v.begin(), v.end())) {
        cur = clean;
        for (int K = 0; K < 3; ++K) {
            for (int i = 0; i < 8; ++i) {
                for (int j = i+1; j < 8; ++j) {
                    if (cur[v[i]].size() == K && cur[v[i]] == cur[v[j]]) {
                        cur[min(v[i],v[j])] += "W";
                        cur[max(v[i],v[j])] += "L";
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < 8; ++i) {
            if (worst[i] == "" || worst[i] > cur[i])
                worst[i] = cur[i];
            if (best[i] == "" || best[i] < cur[i])
                best[i] = cur[i];
        }
        if (j % 100000 == 0)
            cerr << j << " ";
        if (j++ == 10000000) {
            for (int i = 0; i < 8; ++i)
                cerr << i << " " << best[i] << " " << worst[i] << "\n";
            break;
        }
    }

    return 0;
}
