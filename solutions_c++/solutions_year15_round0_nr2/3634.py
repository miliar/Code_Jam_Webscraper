#include <iostream>
#include <map> 
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
using namespace std;

int time(const vector<int>& plates, int splitsize) {
    int t = 0;
    for (int i=0; i < plates.size(); i++) {
        if (plates[i] > splitsize) {
            t += (plates[i]-1)/splitsize;
        } else {
            break;
        }
    }
    return t + min(splitsize, plates[0]);
}

int testcase() {
    int D, n;
    vector<int> plates;
    cin >> D;
    for (int i = 0; i < D; i++) {
        cin >> n;
        plates.push_back(n);
    }
    sort(plates.begin(), plates.end());
    reverse(plates.begin(), plates.end());
    int best = plates[0];
    for (int i = 1; i < plates[0]; i++) {
        best = min(best, time(plates, i));
    }
    return best;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i+1 << ": " << testcase() << endl;
    }
    return 0;
}
