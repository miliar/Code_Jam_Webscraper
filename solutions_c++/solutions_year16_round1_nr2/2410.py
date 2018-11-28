#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;
#define DEBUG 0

void print_all(vector <vector<int> >all) {
    cout << "print all" << endl;
    for(int i = 0; i < all.size(); ++i) {
        vector<int> tmpv = all[i];
        for(int j = 0; j < tmpv.size(); ++j) {
            cout << " " << tmpv[j];
        }
        cout << endl;
    }
}

int map[100][100];
int map_rnd[100][100];
int row_done[100];
int col_done[100];

void print_map(int n) {
    cout << "Print Map" << endl;
    for(int r = 0; r < n; ++r) {
        for(int c = 0; c < n; ++c) {
            cout << " " << map[r][c];
        }
        cout << endl;
    }
}

bool place_sheet(vector< vector<int> >all, int cnt, int n) {
    bool placed = false;
    if(cnt == 2 * n - 1 ) {
//        cout << "done!" << endl;
        return true;
    }
    for(int col = 0; col < n; ++col) {
        if (col_done[col] == 0 && all[cnt][0] == map[0][col]) {
            bool ok = true;
            for(int row = 0; row < n; ++row) {
                if ((map[row][col] != 0) && (map[row][col] != all[cnt][row])) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                for(int i = 1; i < n; ++i) {
                    if (map_rnd[i][col] == 0) {
                        map_rnd[i][col] = cnt;
                        map[i][col] = all[cnt][i];
                    }
                }
                col_done[col] = cnt;
                placed = place_sheet(all, cnt + 1, n);
                if(placed) {
                    if(DEBUG)
                        cout << "placed col: " << col << endl;
                } else {
                    col_done[col] = 0;
                    for(int i = 1; i < n; ++i) {
                        if (map_rnd[i][col] == cnt) {
                            map_rnd[i][col] = 0;
                            map[i][col] = 0;
                        }
                    }
                }
            } 
        }
    }
    if (!placed) {
        for(int row = 1; row < n; ++row) {
            if(row_done[row] == 0 && (map[row][0] == 0) || (all[cnt][0] == map[row][0])) {
                bool ok = true;
                for(int col = 0; col < n; ++col) {
                    if ((map[row][col] != 0) && (map[row][col] != all[cnt][col])) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    for(int i = 0; i < n; ++i) {
                        if (map_rnd[row][i] == 0) {
                            map_rnd[row][i] = cnt;
                            map[row][i] = all[cnt][i];
                        }
                    }
                    row_done[row] = cnt;
                    placed = place_sheet(all, cnt + 1, n);
                    if(placed) {
                        if(DEBUG)
                            cout << "placed row: " << row << endl;
                    } else {
                        row_done[row] = 0;
                        for(int i = 0; i < n; ++i) {
                            if (map_rnd[row][i] == cnt) {
                                map_rnd[row][i] = 0;
                                map[row][i] = 0;
                            }
                        }
                    }
                } 
            }
        }
    }
    return placed;
}

int main() {
    int t;
    cin >> t;
    for (int round = 1; round <= t; ++round) {
        int n;
        cin >> n;

        memset(map, 0, sizeof(map));
        memset(map_rnd, 0, sizeof(map_rnd));
        memset(row_done, 0, sizeof(row_done));
        memset(col_done, 0, sizeof(col_done));
        vector< vector<int> > allsheets(2*n -1);
        for(int i = 0; i < 2 * n - 1; ++i) {
            vector<int> tmpv;
            for(int j = 0; j < n; ++j) {
                int tmpi;
                cin >> tmpi;
                tmpv.push_back(tmpi);
            }
            allsheets[i]= tmpv;
        }

        sort(allsheets.begin(), allsheets.end());

        if(DEBUG) print_all(allsheets);
        for(int i = 0; i < n; ++i) {
            map[0][i] = allsheets[0][i];
            map_rnd[0][i] = 0;
            row_done[0] = 345345;
        }

        place_sheet(allsheets, 1, n);
        if(DEBUG) print_map(n);
        cout << "Case #" << round << ":";
        for(int i = 0; i < n; ++i) {
            if(row_done[i] == 0) {
                for(int j = 0; j < n; ++j) {
                    cout << " " << map[i][j];
                }
                cout << endl;
            }
            if(col_done[i] == 0) {
                for(int j = 0; j < n; ++j) {
                    cout << " " << map[j][i];
                }
                cout << endl;
            }
        }
    }
    return 0;
}
