#include <assert.h>
#include <cstdint>
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

using Num = uint64_t;

Num tileToCheck(int orgTiles, int level) {
    // orgTiles를 체크하는데 orgTiles만큼의 level이면 충분하다.
    /* if (level > orgTiles) level = orgTiles; */

    Num ret = 0;
    for (auto l = level - 1; l >= 0; --l) {
        auto bucketIdx = (level - l - 1);
        if (bucketIdx == 0) continue;
        if (bucketIdx >= orgTiles) break;
        Num bucketSize = std::pow<Num>(orgTiles, l);
        ret += bucketSize * bucketIdx;
    }
    return ret + 1;
}

vector<Num> solve(int orgTiles, int level) {
    vector<Num> solution;

    // tile이 0이면 체크할 필요없다.
    if (orgTiles == 0)
        return solution;

    // tile이 1개면 한번이면 충분.
    if (orgTiles == 1) {
        solution.push_back(1);
        return solution;
    }

    // 현재 solution 넣기
    solution.push_back(tileToCheck(orgTiles, level));
    if (orgTiles <= level) return solution;

    // 다음 solution 넣기
    auto subTiles = orgTiles - level;
    auto subSolution = solve(subTiles, level);
    for (auto s : subSolution) {
        Num offset = ((s - 1) / subTiles) * orgTiles + level;
        solution.push_back(s + offset);
    }

    return solution;
}

int main() {
    int numOfCases;
    cin >> numOfCases;
    for (auto i = 1u; i <= numOfCases; ++i) {
        // read input
        int orgTiles, level, numOfTests;
        cin >> orgTiles >> level >> numOfTests;

        // write output
        cout << "Case #" << i << ":";

        // for small input
        for (auto i = 1u; i <= numOfTests; ++i)
            cout << ' ' << i;
        cout << endl;
        continue;

        auto solution = solve(orgTiles, level);
        if (solution.size() <= numOfTests) {
            for (auto s : solution) cout << ' ' << s;
        } else {
            cout << " IMPOSSIBLE";
        }

        cout << endl;
    }

    return 0;
}
