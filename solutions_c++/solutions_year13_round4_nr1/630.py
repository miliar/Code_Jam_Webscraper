#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <cassert>

#define MOD 1000002013

struct Event {
    long long people;
    int where;
    friend bool operator < (Event a, Event b) {
        return a.where < b.where;
    }
};

using namespace std;

int T, TT;
Event on[1000];
Event off[1000];
long long stations;
int events;

int main() {
    int i, j;
    long long total;
    long long totalCheap;
    long long tripVal;
    
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%lld%d", &stations, &events);
        total = 0;
        totalCheap = 0;
        for (i = 0; i < events; i++) {
            scanf("%d %d %d", &on[i].where, &off[i].where, &on[i].people);
            off[i].people = on[i].people;
            long long d = off[i].where - on[i].where;
            tripVal = d * stations - (d - 1) * d / 2;
            tripVal = tripVal % MOD;
            total += tripVal * on[i].people;
            total = total % MOD;
        }
        sort(on, on+events);
        sort(off, off+events);
        for (i = 0; i < events; i++) {
            for (j = 0; j < events && on[j].where <= off[i].where; j++);
            j--;
            long long p = off[i].people;
            for (; j >= 0 && p >= on[j].people; j--) {
                long long d = off[i].where - on[j].where;
                tripVal = d * stations - (d-1) * d/2;
                tripVal = tripVal % MOD;
                totalCheap += tripVal * on[j].people;
                totalCheap = totalCheap % MOD;
                p -= on[j].people;
                on[j].people = 0;
                assert(j >= 0);
            }
            if (p > 0) {
                long long d = off[i].where - on[j].where;
                tripVal = d * stations - (d-1) * d/2;
                tripVal = tripVal % MOD;
                totalCheap += tripVal * p;
                totalCheap = totalCheap % MOD;
                on[j].people-=p;
                p = 0;
            }
        }
        long long ans = total - totalCheap;
        ans = ans % MOD;
        if (ans < 0)
            ans = ans + MOD;
        printf("%lld\n", ans);
        
        
    }
}