#include <iostream>
#include <sstream> 
#include <cstdio>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdlib> 
#include <ctime>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
template<typename T> T ABS(const T& val) { return val < 0 ? -val : val; }

const size_t MAX_HEIGHT = 1001;

size_t count_steps(size_t cur, size_t targ, vector<size_t>& cache)
{
    if (cur <= targ) {
        return 0;
    } 
    if (cache[cur] != MAX_HEIGHT) {
        return cache[cur];
    }

    size_t cand_split = 1 +
                        count_steps(cur - cur / 2, targ, cache) +
                        count_steps(cur / 2, targ, cache);
    size_t cand_bite = 1 + count_steps(cur - targ, targ, cache);

    cache[cur] = min(cand_split, cand_bite);
    return cache[cur];
}

int main ()
{
    std::ios_base::sync_with_stdio(false);
    size_t T;
    cin >> T;

    for (size_t test = 0; test < T; ++test) {

        size_t N;
        cin >> N;
        vector<size_t> piles(N);

        for (size_t i = 0; i < N; ++i) {
            cin >> piles[i];
        }

        sort(piles.rbegin(), piles.rend());
        size_t bestans = *piles.begin();

        for (size_t level = 1; level <= bestans; ++level) {
            vector<size_t> cache(MAX_HEIGHT, MAX_HEIGHT);
            size_t total_steps = 0;

            for (size_t i = 0; i < piles.size(); ++i) {
                size_t cur_steps = count_steps(piles[i], level, cache);
                total_steps += cur_steps;
            }

            bestans = min(bestans, total_steps + level);
        }

        cout << "Case #" << test + 1 << ": " << bestans << "\n";
    }


    return 0;
}
