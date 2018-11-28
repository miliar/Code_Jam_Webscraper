#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 

#define equal equalll
#define less lesss
const int N = 1e5;
const int INF = 1e9;

long long e[N];
long long f[N];
int k;

void read() {
    scanf("%d", &k);
    for (int i = 0; i < k; i++)
        scanf("%lld", &e[i]);
    for (int i = 0; i < k; i++)
        scanf("%lld", &f[i]);
}

void solve() {
    long long mn = -e[0]; 
    for (int i = 0; i < k; i++)
        e[i] += mn;

    long long sum = 0;   
    for (int i = 0; i < k; i++)
        sum += f[i];
            
    int n = 0;
    for (; (1ll << n) < sum; n++);
    assert((1ll << n) == sum);

    map < long long , int > q;
    for (int i = 0; i < k; i++)
        q[e[i]] = i;
    vector < long long > answer;
    
    f[q[0]]--;
    for (int i = 0; i < n; i++) {
        //cerr << "========================\n";
        int mn = -1;
        for (int j = 0; j < k; j++)
            if (f[j] != 0) {
                mn = e[j];
                break;
            }
        //db(mn);
        assert(mn != -1);
        for (int mask = 0; mask < (1 << answer.size()); mask++) {
            long long s = mn;
            for (int i = 0; i < (int)answer.size(); i++)
                if (((mask >> i) & 1) == 1)
                    s += answer[i];
            //db(s);
            assert(q.count(s) == 1); 
            int id = q[s];
            assert(f[id] > 0);
            f[id]--;
        }
        //for (int i = 0; i < k; i++)
            //db2(e[i], f[i]);
        answer.pb(mn);
    } 
    sort(answer.begin(), answer.end());
    reverse(answer.begin(), answer.end());
    int resMask = -1;
    for (int mask = 0; mask < (1ll << n); mask++) {
        long long s = 0;
        for (int i = 0; i < n; i++)
            if (((mask >> i) & 1) == 1)
                s += answer[i]; 
        if (s == mn) {
            resMask = mask;
            break;
        }
    }
    for (int i = 0; i < n; i++)
        if (((resMask >> i) & 1) == 1)
           answer[i] *= -1; 
    sort(answer.begin(), answer.end()); 
    for (auto x: answer)
        printf("%lld ", x);
    printf("\n");


}

void printAns() {

}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("Dsmall.in", "r", stdin);
    freopen("Dsmall.out", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: ", tt + 1);
            read();
            solve();
            printAns();
        }
    }
    else {
        stress();
    }

    return 0;
}

