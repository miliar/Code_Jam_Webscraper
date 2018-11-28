#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    size_t nfields = 0;
    cin >> nfields;

    for(size_t ifield = 1 ; ifield <= nfields ; ++ifield) {
        cout << "Case #" << ifield << ": ";
        size_t w, h;
        cin >> h >> w;
        vector<vector<size_t>> field(h, vector<size_t>(w, 0));
        vector<size_t> max_horiz(h, 0), max_vert(w, 0);
        // First, read-in the field, and compute the maximums on the fly.
        for(size_t y = 0 ; y < h ; ++y) {
            for(size_t x = 0 ; x < w ; ++x) {
                cin >> field[y][x];
                max_horiz[y] = max(max_horiz[y], field[y][x]);
                max_vert[x] = max(max_vert[x], field[y][x]);
            }
        }

        // Check every field for possibility, using e[y][x] >= min(max_horiz[i])
        for(size_t y = 0 ; y < h ; ++y) {
            for(size_t x = 0 ; x < w ; ++x) {
                if(field[y][x] < min(max_horiz[y], max_vert[x])) {
                    cout << "NO" << endl;
                    // PURE EVILESS!!
                    goto next;
                }
            }
        }

        cout << "YES" << endl;
next:
        (void*)0;
    }

    return 0;
}
