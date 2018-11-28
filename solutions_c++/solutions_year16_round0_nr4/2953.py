#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

bool incrementPattern(string &pattern) {
    for(int i = pattern.size() - 1; i >= 0; --i) {
        if(pattern[i] == 'G') {
            pattern[i] = 'L';
            return true;
        } else {
            pattern[i] = 'G';
        }
    }

    return false;
}

string fractile(const string& original, int C) {
    if(C <= 1) {
        return original;
    } else {
        string prev = fractile(original, C - 1);
        string pattern;
        for(char c : prev) {
            if(c == 'G') {
                pattern.append(string(original.size(), 'G'));
            } else {
                pattern.append(original);
            }
        }

        return pattern;
    }
}

void printPossibilities(int K, int C) {
    string pattern(K, 'G');

    do {
        cout << pattern << " => " << fractile(pattern, C) << endl;
    } while(incrementPattern(pattern));

    cout << " -- -- -- " << endl;

    string allLead(K, 'L');
    for(int i = 0 ; i < K; i++) {
        string oneGold = allLead;
        oneGold[i] = 'G';
        cout << oneGold << " => " << fractile(oneGold, C) << endl;
    }
}

void printTrivialSolution(int K) {
    for(int i = 1; i <= K; i++) {
        cout << " " << i;
    }
}

// outputs 0-based indices for tiles
set<uint64_t> miniumTileSet(int K, int C) {
    set<uint64_t> tiles;
    
    int unknownRootTile = 0;
    while(unknownRootTile < K) {
        uint64_t tileToCheck = 0;
        for(int level = C - 1; level >= 0 && unknownRootTile < K; level--, unknownRootTile++) {
            tileToCheck += unknownRootTile * pow(K, level);
        }
        
        tiles.insert(tileToCheck);
    }

    return tiles;
}

void printFullSolution(int K, int C, int S) {
    auto tilesToLookAt = miniumTileSet(K, C);
    if(tilesToLookAt.size() <= (size_t) S) {
        for(auto tile : tilesToLookAt) {
            cout << " " << tile + 1;
        }
    } else {
        cout << " IMPOSSIBLE";
    }
}

int main() {
    int numCases;
    cin >> numCases;
    
    for(int caseNum = 1; caseNum <= numCases; ++caseNum) {
        // do not print space after colon, for easy set printing
        cout << "Case #" << caseNum << ":";

        int K, C, S;
        cin >> K >> C >> S;
        if(S == 0) {
            printPossibilities(K, C);
        //} else {
        //    printFullSolution(K, C, S);
        //}
        } else if(K == S) {
            printTrivialSolution(K);
        } else {
            cout << " IMPOSSIBLE";
        }

        cout << endl;
    }
}
