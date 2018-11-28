#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "functional"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int mainA() {
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    fflush(stderr);
    int n;
    scanf("%d", &n);
    //priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> queue;
    priority_queue<pair<int, char>> queue;
    for (int i = 0; i < n; i++) {
        int p;
        scanf("%d", &p);
        queue.push(make_pair(p, 'A' + i));
    }
    printf("Case #%d:", Ti);
    while (!queue.empty()) {
        auto pair1 = queue.top();
        queue.pop();
        if (!queue.empty()) {
            auto pair2 = queue.top();
            if (pair1.first > pair2.first || (pair1.first == 1 && queue.size() == 2))
                printf(" %c", pair1.second);
            else {
                printf(" %c%c", pair1.second, pair2.second);
                queue.pop();
                if (pair2.first > 1)
                    queue.push(make_pair(pair2.first - 1, pair2.second));
            }
            if (pair1.first > 1)
                queue.push(make_pair(pair1.first - 1, pair1.second));
        }
        else
        {
            int i = pair1.first;
            while (i > 1) {
                printf(" %c%c", pair1.second, pair1.second);
                i -= 2;
            }
            if (i > 0)
                printf(" %c", pair1.second);
        }
    }
    printf("\n");
    fflush(stdout);
  }
  return 0;
}
