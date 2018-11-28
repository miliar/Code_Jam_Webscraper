#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define pb push_back
#define mp make_pair
#define EPS 1.0e-8
#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef long double ld;

int bestTime;

void bktk(priority_queue<int> pq, int time) {
    if (time >= bestTime) return;

    int top = pq.top(); pq.pop();
    bestTime =  min(bestTime, top + time);

    int halfTop = top/2;
    priority_queue<int> pq_copy;
    for(int i = 2; i<=halfTop; i++) {
        pq_copy = pq;
        pq_copy.push(i);
        pq_copy.push(top-i);
        bktk(pq_copy, time+1);
    }
}

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    int T;
    int d, p;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d", &d);
        priority_queue<int> pq;
        while(d--) {
            scanf("%d", &p);
            pq.push(p);
        }

        bestTime = pq.top();
        bktk(pq, 0);

        printf("Case #%d: %d\n", ncase, bestTime);
    }

    return 0;
}
