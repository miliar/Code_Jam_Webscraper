/*************************************************************************
	> File Name: ./qua_B.cpp
	> Author: 
	> Mail: 
	> Created Time: 2015年04月11日 星期六 22时29分23秒
 ************************************************************************/

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1000 + 10;

int plates[maxn];

int main() {
    int T;

    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase++) {
        int n;
        scanf("%d", &n);
        int maxp = 0;
        memset(plates, 0, sizeof(plates));
        for(int i = 0; i < n; i++) {
            int t;
            scanf("%d", &t);
            maxp = max(maxp, t);
            plates[t]++;
        }
        int sum = 0;
        while(maxp > 1) {
            if(plates[maxp] <= 0) {
                maxp--;
                continue;
            }
            int current = maxp;
            int halfOfCur = current - current / 2;
            int tp = maxp;
            int cost = 0;
            while(tp > 0 && tp > halfOfCur) {
                if(plates[tp] <= 0) {
                    tp--;
                    continue;
                }
                cost += plates[tp];
                plates[tp / 2] += plates[tp];
                plates[tp - tp/2] += plates[tp];
                tp--;
            }
            if(cost <= maxp - halfOfCur) {
                sum += cost;
                maxp = tp;
            } else {
                break;
            }
        }

        if(maxp > 0) {
            sum += maxp;
        }

        printf("Case #%d: %d\n", kase, sum);
    }

    return 0;
}
