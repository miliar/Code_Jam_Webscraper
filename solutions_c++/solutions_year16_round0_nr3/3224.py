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

bool f[1000000000];
vector<int> p;

void seive() {
    for (int i=2; i<=(int)sqrt(1000000000); i++) {
        if (!f[i]) {
            for (int j=i*2; j<(1000000000); j+=i) {
                f[j] = 1;
            }
        }
    }
    for (int i=2; i<(1000000000); i++) {
        if (!f[i]) p.push_back(i);
    }
}


int main() {
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    seive();
    for (int t=1; t<=T; t++) {
        int N, J;
        int d[11];
        scanf("%d%d", &N, &J);
        printf("Case #%d: \n", t);

        for (int i=0; i<(1<<(N-2)) && J; i++) {
            int c = (1<<(N-1)) | (i<<1) | 1;
            bool hasD;
            for (int b=2; b<=10; b++) {
                hasD = 0;
                long long k = 0;
                for (int j=N-1; j>=0; j--) {
                    if (c&(1<<j)) k = k * b + 1;
                    else k = k * b;
                }
                for (int j=0; j<p.size(); j++) {
                    if (k > p[j] && k % p[j] == 0) {
                        d[b] = p[j];
                        hasD = 1;
                        break;
                    }
                }
                if (!hasD) {
                    break;
                }
            }
            if (hasD) {
                J -= 1;
                for (int j=N-1; j>=0; j--) printf("%d", c&(1LL<<j)?1:0);
                for (int j=2; j<=10; j++) printf(" %d", d[j]);
                printf("\n");
            }
        }
    }
}