#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>
#include <iostream>

using namespace std;

#define INF 1000000007
#define MAXN 1000002
#define MAXTAM 10000002

int inverter(int x) {
    int res=0;
    while (x!=0) {
        res=res*10+x%10;
        x=x/10;
    }
    return res;
}

int dist[MAXTAM];
queue<int> fila;

void bfs() {
    memset(dist, -1, sizeof(dist));
    dist[1]=1;
    fila.push(1);
    while (!fila.empty()) {
        int x=fila.front();
        fila.pop();
        int y;
        y=x+1;
        if (dist[y]==-1 && y<MAXTAM) {
            dist[y]=dist[x]+1;
            fila.push(y);
        }
        y=inverter(x);
        if (dist[y]==-1 && y<MAXTAM) {
            dist[y]=dist[x]+1;
            fila.push(y);
        }
    }
}

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0_saida.txt", "w", stdout);
    bfs();
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %d\n", teste, dist[n]);
    }
    return 0;
}
