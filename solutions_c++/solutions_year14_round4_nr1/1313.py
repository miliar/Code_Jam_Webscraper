#include <algorithm>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

int sizes[20000];
int slots[20000][2];
int nfiles, cap, slotcount;

int dfs(int combo, int filesleft) {
    if (filesleft == 0) {
        return slotcount;
    }
    int best = nfiles;
    for (int i = 0; i < nfiles; i++) {
        if ((combo & (1 << i)) == 0) {
            combo += (1 << i);
            if (slotcount == 0) {
                slots[0][0] = sizes[i];
                slots[0][1] = 0;
                slotcount++;
                best = min(best, dfs(combo, filesleft - 1));
                slotcount--;
            } else if (slots[slotcount-1][1] == 0 && slots[slotcount-1][0] + sizes[i] <= cap) {
                slots[slotcount-1][1] = sizes[i];
                best = min(best, dfs(combo, filesleft - 1));
                slots[slotcount-1][1] = 0;
            } else {
                slots[slotcount][0] = sizes[i];
                slots[slotcount][1] = 0;
                slotcount++;
                best = min(best, dfs(combo, filesleft - 1));
                slotcount--;
            }
            combo -= (1 << i);
        }
    }
    return best;
}

int main() {
    int ncase;
    cin >> ncase;
    for (int csnum = 1; csnum <= ncase; csnum++) {
        cin >> nfiles >> cap;
        vector<int> blah;
        for (int i = 0; i < nfiles; i++) {
            cin >> sizes[i];
            blah.push_back(sizes[i]);
        }
        slotcount = 0;
        //int res = dfs(0, nfiles);
        sort(blah.begin(), blah.end());
        bool seen[nfiles];
        int res = 0;
        memset(seen, 0, sizeof(seen));
        for (int i = blah.size() - 1; i >= 0; i--) {
            if (seen[i]) continue;
            for (int j = i-1; j >= 0; j--) {
                if (seen[j]) continue;
                if (blah[i] + blah[j] <= cap) {
                    seen[j] = true;
                    break;
                }
            }
            seen[i] = true;
            res++;
        }
        cout << "Case #" << csnum << ": " << res << endl;
    }
}
