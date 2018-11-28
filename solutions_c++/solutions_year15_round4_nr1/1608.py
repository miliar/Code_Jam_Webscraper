#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <bitset>
#include <numeric>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int, int> PII;
typedef long long ll;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int main() {
	int _; cin >> _; 
	for (int __ = 1; __ <= _; __ ++) {
        
        printf ("Case #%d: ", __);
        int R, C;
        cin >> R >> C;
        vector<vector<int> > grid(R, vector<int>(C, 0));
        vector<vector<int> > result(R, vector<int>(C, 0));
        bool shouldskip = false;
        
        
        
        for (int i = 0; i < R; ++i) {
           for (int j = 0; j < C; ++j) {
              char arrow;
              cin >> arrow;
              if (arrow == '.') {
                 grid[i][j] = 0;
              } else if (arrow == '^') {
                 grid[i][j] = 1;
              } else if (arrow == 'v') {
                 grid[i][j] = 2;
              } else if (arrow == '<') {
                 grid[i][j] = 4;
              } else {
                 grid[i][j] = 8;
              }
           }
        }
        
        
        // from left
        for (int i = 0; i < R; ++i) {
           for (int j = 0; j < C; ++j) {
              result[i][j] |= 4;
              if (grid[i][j] != 0) {
                 break;
              }
           }
        }
        
        // from right
        for (int i = 0; i < R; ++i) {
           for (int j = C-1; j >=0; --j) {
              result[i][j] |= 8;
              if (grid[i][j] != 0) {
                 break;
              }
           }
        }
        
        // from up
        for (int j = 0; j < C; ++j) {
           for (int i = 0; i < R; ++i) {
              result[i][j] |= 1;
              if (grid[i][j] != 0) {
                 break;
              }
           }
        }
        // from down
        for (int j = 0; j < C; ++j) {
           for (int i = R - 1; i >=0; --i) {
              result[i][j] |= 2;
              if (grid[i][j] != 0) {
                 break;
              }
           }
        }
        
        int res = 0;
        

        
        for (int i = 0; i < R; ++i) {
           for (int j = 0; j < C; ++j) {
              if (result[i][j] == 15 && grid[i][j] != 0) {
                 shouldskip = true;
                 break;
              } else {
                 if (grid[i][j] & result[i][j]) {
                    res++;
                 }
              }
           }
           if (shouldskip) {
              break;
           }
        }
        
        if (shouldskip) {
           printf ("IMPOSSIBLE\n");
        } else {
           printf ("%d\n", res);
        }
	}
	return 0; 
}
