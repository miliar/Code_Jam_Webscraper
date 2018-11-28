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

int mat[5][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};

bool testvalid(vector<int> &tmp, int start, int end, int goal) {
     if (start == end) {
        return tmp[start] == goal;
     } else {
         int sign = 1;
         int a = tmp[start];
         for (int i = start + 1; i <= end; ++i) {
             a = mat[a][tmp[i]];
             if (a < 0) {
                a = a * -1;
                sign *= -1;
             }
         }
         a = a * sign;
         return a == goal;
     }
}

int main() {
	int _; cin >> _; 
	for (int __ = 1; __ <= _; __ ++) {
        printf ("Case #%d: ", __);
        int L, X;
        string str;
        cin >> L >> X >> str;
        string tmp;
        while (X-- > 0) {
              tmp += str;
        }
        if (tmp.size() < 3) {
            printf ("NO\n");
            continue;
        }
        bool same = true;
        int head = tmp[0] - 'i' + 2;
        vector<int> tmp2(tmp.size(), 0);
        for (int i = 0; i < tmp.size(); ++i) {
            tmp2[i] = tmp[i] - 'i' + 2;
            if (head != tmp2[i]) {
               same = false;
            }
        }
        if (same) {
            printf ("NO\n");
            continue;
        }
        
        if (!testvalid(tmp2, 0, tmp.size() - 1, -1)) {
            printf ("NO\n");
            continue;
        }
        
        bool find = false;
        for (int i = 0; i < tmp.size() - 2; ++i) {
            if (!testvalid(tmp2, 0, i, 2)) continue;
            for (int j = i + 1; j < tmp.size() - 1; ++j) {
                    if (testvalid(tmp2, i+1, j, 3) && testvalid(tmp2, j+1, tmp.size() - 1, 4)) {
                       find = true;
                       break;   
                    }
                }
                if (find) break;
        }
        if (find) {
           printf ("YES\n");
        } else  {
           printf ("NO\n");
        }
        
	}
	return 0; 
}
