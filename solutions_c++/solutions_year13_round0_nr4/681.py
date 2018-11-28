#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;

int T, K, N;
list<int> keys;
vector<int> chestT;
vector<vector<int> > chestK;
list<int> track;

set<set<int> > cacheNegative;

bool solve(const list<int>& keys, set<int>& openedChests)
{
	if (openedChests.size() == N) return true;

	set<set<int> >::iterator cacheIt = cacheNegative.find(openedChests);
	if (cacheIt != cacheNegative.end())
		return false;

    for (int nn = 1; nn <= N; ++nn) {
        if (openedChests.find(nn) == openedChests.end()) {
            // try to open it
            int needKey = chestT[nn - 1];
            list<int>::const_iterator keyIt = find(keys.begin(), keys.end(), needKey);
            if (keyIt != keys.end()) {
                list<int> keys1 = keys;
                keys1.erase(find(keys1.begin(), keys1.end(), needKey));
                keys1.insert(keys1.end(), chestK[nn - 1].begin(), chestK[nn - 1].end());

                track.push_back(nn);
                openedChests.insert(nn);
                if (solve(keys1, openedChests))
                    return true;
                openedChests.erase(nn);
                track.pop_back();
            }
        }
    }
	cacheNegative.insert(openedChests);
    return false;
}

int main(int argc, char* argv[])
{
    chestT.reserve(256);
    chestK.reserve(256);
    cin >> T;
    for (int t = 0; t != T; ++t) {
        cin >> K >> N;
        keys.clear();
        track.clear();
		cacheNegative.clear();
        for (int k = 0; k != K; ++k) {
            int key;
            cin >> key;
            keys.push_back(key);
        }
        chestT.resize(N);
        chestK.resize(N);
        for (int n = 0; n != N; ++n) {
            int Kn;
            cin >> chestT[n] >> Kn;
            chestK[n].resize(Kn);
            for (int kn = 0; kn != Kn; ++kn)
                cin >> chestK[n][kn];
        }
        set<int> openedChests;
        if (solve(keys, openedChests)) {
            cout << "Case #" << (t + 1) << ":";
            for (list<int>::const_iterator it = track.begin();
                    it != track.end(); ++it) {
                cout << " " << *it;
            }
            cout << "\n";
        }
        else {
            cout << "Case #" << (t + 1) << ": IMPOSSIBLE\n";
        }
    }
    return 0;
}

