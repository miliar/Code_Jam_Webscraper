#include <vector>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <assert.h>

using namespace std;

struct Node {
    
};

int lawn[105][105];
bool isVisited[105][105];
int main() {
    int T;
    scanf("%d", &T);
    for (int index = 1; index <= T; ++index) {
        int N, M;
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                scanf("%d", &lawn[i][j]);
                isVisited[i][j] = false;
            }
        }
        int xmin = -1, ymin = -1, hmin = 101;
        bool possible = true;
        while (true) {
            xmin = -1, ymin = -1, hmin = 101;
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < M; ++j) {
                    if (!isVisited[i][j] && lawn[i][j] < hmin) {
                        xmin = i;
                        ymin = j;
                        hmin = lawn[i][j];
                    }
                }
            }
            if (xmin == -1)
                break;
            bool isRow = true, isCol = true;
            //check row
            for (int j = 0; j < M; ++j) {
                if (!isVisited[xmin][j] && lawn[xmin][j] != hmin) {
                    isRow = false;
                    break;
                }
            }
            if (isRow) {
                for (int j = 0; j < M; ++j) {
                    isVisited[xmin][j] = true;
                }
            }
            else {
                for (int i = 0; i < N; ++i) {
                    if (!isVisited[i][ymin] && lawn[i][ymin] != hmin) {
                        isCol = false;
                        break;
                    }
                }
                if (isCol) {
                    for (int i = 0; i < N; ++i) {
                        isVisited[i][ymin] = true;
                    }
                }
            }
            if ((!isRow) && (!isCol))
                possible = false;
            if (!possible)
                break;
        }
        if (!possible)
            cout<<"Case #"<<index<<": NO"<<endl;
        else
            cout<<"Case #"<<index<<": YES"<<endl;
    }
    return 0;
}