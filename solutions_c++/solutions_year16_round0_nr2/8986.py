#include <iostream>
#include <cstdint>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

// We could use uint64_t, but it won't work for the large inputs
// So let's use strings
char flip(char c) { return (c == '+') ? '-' : '+'; }

// This method is "symmetric"
void flipTopN(string& s, int n) {
    string tmp(s);
    // Slower, but safer
    for (int i = 0; i < n; ++i) {
        s[n - i - 1] = flip(tmp[i]);
    }
}

bool isDone(const string& s) {
    bool res = true;
    for (auto c : s) {
        if (c == '-') {
            res = false; break;
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string inS;
        cin >> inS;
        cout << "Case #" << t << ": ";
        //cout << inS << endl;
        //flipTopN(inS, inS.length()); 
        //flipTopN(inS, 1); 
        // Do one transform at a time until you find a solution, then break
        bool done = false;
        int res = 0;
        // Create iteration vector
        if (!isDone(inS)) {
            int inLen = inS.length();
            for (int j = 1; j <= inLen; ++j) {
                vector<vector<int>> vv;
                vector<bool> vIdx(inLen);
                fill(vIdx.begin() + inLen - j, vIdx.end(), true);

                // I'm making some assumptions about the structure 
                do {
                    vector<int> vCurr;
                    for (int i = 0; i < inLen; ++i) {
                        if (vIdx[i]) {
                            vCurr.push_back(i+1);
                        }
                    }
                    vv.push_back(vCurr);
                } while (next_permutation(vIdx.begin(), vIdx.end()));

                // TODO:
                // This shows that we are NOT rearranging them 
                // We should revisit this
                //for (auto v : vv) {
                    //for (auto x : v) {
                        //cout << x << " ";
                    //}
                    //cout << endl;
                //}
                //cout << endl;
                //cout << endl;

                for (auto v : vv) {
                    string sCurr{inS};
                    for (int i = 0; i < v.size(); ++i) {
                        flipTopN(sCurr, v[i]); 
                        if (isDone(sCurr)) {
                            //cout << "  FOUND   "; // We ARE finding the solution in this case
                            res = i + 1;
                            done = true;
                            break;
                        }
                    }
                    if (done) {
                        break;
                    }
                }
                if (done) {
                    break;
                }
            }
        }
        cout << res << endl;
    }
}
