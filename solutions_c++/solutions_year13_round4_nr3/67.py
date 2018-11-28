#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

vector<int> ge[2000];
int x[2000], a[2000], b[2000], ind[2000], s[2000];

void insertEdge(int a, int b) {
    ge[b].push_back(a);
    //ge[a].push_back(b);
}

void work() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++) {
        ge[i].clear();
    }
    for (int i = 0; i < n; i ++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; i ++) {
        scanf("%d", &b[i]);
    }
    for (int i = 0; i < n; i ++) {
        for (int j = i - 1; j >= 0; j --) {
            if (a[i] == a[j]) {
                insertEdge(i, j);
                break;
            }
        }
        for (int j = i - 1; j >= 0; j --) {
            if (a[j] + 1 == a[i]) {
                insertEdge(j, i);
                break;
            }
        }
    }
    for (int i = 0; i < n; i ++) {
        for (int j = i + 1; j < n; j ++) {
            if (b[i] == b[j]) {
                insertEdge(i, j);
                break;
            }
        }
        for (int j = i + 1; j < n; j ++) {
            if (b[j] + 1 == b[i]) {
                insertEdge(j, i);
                break;
            }
        }
    }
    memset(ind, 0, sizeof(ind));
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < ge[i].size(); j ++)
            ind[ge[i][j]] ++;
    priority_queue<int> pq;
    for (int i = 0; i < n; i ++)
        if (ind[i] == 0) pq.push(i);
    for (int i = n - 1; i >= 0; i --) {
        int t = pq.top();
        pq.pop();
        x[t] = i + 1;
        for (int j = 0; j < ge[t].size(); j ++) {
            ind[ge[t][j]] --;
            if (ind[ge[t][j]] == 0) pq.push(ge[t][j]);
        }
    }
    for (int i = 0; i < n; i ++) {
        if (i < n - 1) {
            printf("%d ", x[i]);
        } else {
            printf("%d\n", x[i]);
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test ++) {
        printf("Case #%d: ", test + 1);
        work();
    }

    return 0;
}