#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

int T;
int n;
int ans[10000];
int pre[10000];
int w, h, b;


struct Block{
    int x0, y0, x1, y1;
} blocks[10000];

int edges[2000][2000];

int abs(int a) { return a > 0 ? a : -a; }
int min(int a, int b) { return a < b ? a : b; }
int max(int a, int b) { return a > b ? a : b; }

int countleft(int i, int j)
{
    // i  --> j
    bool xoverlap = 
     ((blocks[i].x0 >= blocks[j].x0 - 1 && 
        blocks[i].x0 <= blocks[j].x1 + 1) ||
        (blocks[i].x1 >= blocks[j].x0 - 1 &&
         blocks[i].x1 <= blocks[j].x1 + 1) ||
        (blocks[j].x0 >= blocks[i].x0 - 1 && 
         blocks[j].x0 <= blocks[i].x1 + 1) ||
        (blocks[j].x1 >= blocks[i].x0 - 1 &&
         blocks[j].x1 <= blocks[i].x1 + 1));
    bool yoverlap = 
     ((blocks[i].y0 >= blocks[j].y0 - 1 && 
        blocks[i].y0 <= blocks[j].y1 + 1) ||
        (blocks[i].y1 >= blocks[j].y0 - 1 &&
         blocks[i].y1 <= blocks[j].y1 + 1) ||
        (blocks[j].y0 >= blocks[i].y0 - 1 && 
         blocks[j].y0 <= blocks[i].y1 + 1) ||
        (blocks[j].y1 >= blocks[i].y0 - 1 &&
         blocks[j].y1 <= blocks[i].y1 + 1));
    if (xoverlap && yoverlap) {
        return 0;
    }
    if (xoverlap) {
        int ret = 
            min(
            min(abs(blocks[i].y0 - blocks[j].y0),
                abs(blocks[i].y0 - blocks[j].y1)),
            min(abs(blocks[i].y1 - blocks[j].y0),
                abs(blocks[i].y1 - blocks[j].y1))
            );
        return ret-1;
    }
    if (yoverlap) {
        int ret = 
            min(
                    min(abs(blocks[i].x0 - blocks[j].x0),
                        abs(blocks[i].x0 - blocks[j].x1)),
                    min(abs(blocks[i].x1 - blocks[j].x0),
                        abs(blocks[i].x1 - blocks[j].x1))
               );
        return ret-1;
    }

    int ret;
        ret = max(
                min(abs(blocks[i].x1 - blocks[j].x0),
                    abs(blocks[i].x0 - blocks[j].x1)),
                min(abs(blocks[i].y1 - blocks[j].y0),
                    abs(blocks[i].y0 - blocks[j].y1)));

        return ret - 1;

}

int count(int i, int j)
{
    // i   j
    return min(countleft(i, j), countleft(j, i));
}

int v[10000];
const int inf = 2000000000;

int solve()
{
    for (int i=0; i<b+2; ++i) {
        edges[i][i] = 0;
    }
    for (int i=0; i<b; ++i) {
        for (int j=0; j<b; ++j) {
            edges[i][j] = edges[j][i] = count(i, j);
        }
    }
    for (int i=0; i<b; ++i) {
        // src b
        edges[i][b] = edges[b][i] = blocks[i].x0;
        // dst b+1
        edges[i][b+1] = edges[b+1][i] = w - blocks[i].x1 - 1;
    }
    edges[b][b+1] = w;
    edges[b+1][b] = w;
    

    n = b + 2;
    /*
    for (int i=0; i<n; ++i) {
        for (int j=0; j<n; ++j) {
            printf("%d ", edges[i][j]);
        }
        putchar('\n');
    }
    */
    int src = b;
    int dst = b + 1;
    for (int i=0; i<n; ++i) {
        ans[i] = inf; v[i] = 0; pre[i] = -1;
    }
    ans[src] = 0;
    for (int j=0; j<n; ++j) {
        int k = -1;
        for (int i=0; i<n; ++i) {
            if (!v[i] && (k == -1 || ans[i] < ans[k])) k = i;
        }

        v[k] = 1;
        for (int i=0; i<n; ++i) {
            if (!v[i] && (ans[k] + edges[k][i] < ans[i])) {
                ans[i] = ans[k] + edges[k][i];
                pre[i] = k;
            }
        }
    }
    return ans[dst];
}

int main()
{
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cin >> w >> h >> b;
        for (int i=0; i<b; ++i) {
            cin >> blocks[i].x0
                >> blocks[i].y0
                >> blocks[i].x1
                >> blocks[i].y1;
        }
        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}
