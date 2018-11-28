#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ifstream inf("B-large.in");
    ofstream ouf("output.txt");
    int T; inf >> T;
    for(int t = 0; t < T; ++t) {
        int D; inf >> D;
        vector<int> P(D);
        for(int i = 0; i < D; ++i) {
            inf >> P[i];
        }
        int answer = numeric_limits<int>::max();
        for(int max_left = *max_element(P.begin(), P.end()); max_left >= 1; --max_left) {
            int penalty = 0;
            for(int i = 0; i < P.size(); ++i) {
                if(P[i] > max_left) {
                    penalty += (P[i] + max_left - 1) / max_left - 1;
                }
            }
            answer = min(answer, penalty + max_left);
        }
        ouf << "Case #" << t + 1 << ": " << answer << endl;
    }
    return 0;
}