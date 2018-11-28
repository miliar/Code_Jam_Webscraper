#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cassert>
#include <limits>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>

using namespace std;

void minDiscsBrute(const vector<int>& S, int X, vector<bool> matched, int numMatched, int& solution) {
    int from = -1;
    for (int i = 0; i != S.size(); ++i) {
        if (!matched[i]) {
            matched[i] = true;
            for (int j = 0; j != S.size(); ++j) {
                if (!matched[j] && (S[i] + S[j] <= X)) {
                    matched[j] = true;
                    minDiscsBrute(S, X, matched, numMatched + 2, solution);
                    matched[j] = false;
                }
            }
            matched[i] = false;
        }
    }

    solution = min(solution, (numMatched / 2) + (int(S.size()) - numMatched));
}

int minDiscsBrute(const vector<int>& S, int X) {
    vector<bool> matched(S.size());
    int soln = numeric_limits<int>::max();
    minDiscsBrute(S, X, matched, 0, soln);
    return soln;
}

// functions to compute maximum size matching and maximal independent set in a bipartite graph

struct Bipartite
{
    Bipartite(int numLeft, int numRight)
        : Left(numLeft)
        , NumRight(numRight)
    {
    }

    void addEdge(int left, int right) {
        assert(left < Left.size() && right < NumRight);
        Left[left].push_back(right);
    }

    vector<vector<int> > Left;
    int NumRight;
};

bool extendMatching(vector<int>& matchingLeft,
                    vector<int>& matchingRight,
                    const Bipartite& G) {
    
    // BFS.  start with all unmatched lhs verts
    queue<int> Q;
    int NumLeft = G.Left.size();
    vector<int> predecessorL(matchingLeft.size(), -1);
    vector<int> predecessorR(matchingRight.size(), -1);

    for (int i = 0; i != NumLeft; ++i) {
        if (matchingLeft[i] == -1) {
            Q.push(i);
            predecessorL[i] = -2; // special value, shows reached but predecessor is sink
        }
    }

    while (!Q.empty()) {
        int idx = Q.front();
        Q.pop();

        if (idx < NumLeft) {
            // vtx on lhs, can explore all edges except one that's
            // already in the matching
            const vector<int>& rhsVerts = G.Left[idx];
            int ignoreVert = matchingLeft[idx];
            for (size_t i = 0; i != rhsVerts.size(); ++i) {
                int rtIdx = rhsVerts[i];
                if (rtIdx != ignoreVert && predecessorR[rtIdx] == -1) {
                    Q.push(rtIdx + NumLeft);
                    predecessorR[rtIdx] = idx;
                }
            }
        } else {
            // vtx on rhs, two cases:
            idx -= NumLeft;
            if (matchingRight[idx] == -1) {
                // Unmatched, can finish search.  Follow predecessor
                // links to modify matching.
                bool right = true;
                int cur = idx;
                while (cur >= 0) {
                    if (right) {
                        int lftIdx = predecessorR[cur];
                        matchingRight[cur] = lftIdx;
                        matchingLeft[lftIdx] = cur;
                        cur = lftIdx;
                    } else {
                        cur = predecessorL[cur];
                    }
                    right = !right;
                }
                return true;
            } else {
                // Matched, can explore back to lhs
                size_t lftIdx = matchingRight[idx];
                if (predecessorL[lftIdx] == -1) {
                    Q.push(lftIdx);
                    predecessorL[lftIdx] = idx;
                }
            }
        }
    }

    // didn't find way to extend
    return false;
}

int maximalMatching(const Bipartite& G) {
    vector<int> matchingL(G.Left.size(), -1);
    vector<int> matchingR(G.NumRight, -1);
    int matchingSize = 0;
    while (extendMatching(matchingL, matchingR, G)) {
        ++matchingSize;
    }

    // obviously could output the matching itself if we wanted to ... 
    return matchingSize;
}

int minDiscs(const vector<int>& S, int X) {
    vector<int> lhs;
    vector<int> rhs;
    for (int i = 0; i != S.size(); ++i) {
        if (S[i] > X/2) {
            lhs.push_back(i);
        } else {
            rhs.push_back(i);
        }
    }

    if (lhs.empty()) {
        // all files can be paired up
        return (S.size() + 1) / 2;
    } else if (rhs.empty()) {
        // no files can be paired up
        return S.size();
    }

    Bipartite G(lhs.size(), rhs.size());
    for (int i = 0; i != lhs.size(); ++i) {
        int left = lhs[i];
        for (int j = 0; j != rhs.size(); ++j) {
            int right = rhs[j];

            if (S[left] + S[right] <= X) {
                G.addEdge(i, j);
            }
        }
    }

    int numPaired = maximalMatching(G);
    int numLargeRemaining = lhs.size() - numPaired;
    int numSmallRemaining = rhs.size() - numPaired;
    return numPaired + numLargeRemaining + (numSmallRemaining + 1) / 2;
}

int main() {
    // ifstream in("sample.in");
    istream& in = cin;

    int C;
    in >> C;
    for (int c = 0; c != C; ++c) {
        int N, X;
        in >> N >> X;
        vector<int> S(N);
        for (int i = 0; i != N; ++i) {
            in >> S[i];
        }
        cout << "Case #" << (c+1) << ": " << minDiscs(S, X) << endl;
    }
    return 0;
}
