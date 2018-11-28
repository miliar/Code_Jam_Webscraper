#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int K, C, S;
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", t);
        for (int j=1; j<=K; j++) {
            printf(" %d", j);
        }
        printf("\n");
    }
}