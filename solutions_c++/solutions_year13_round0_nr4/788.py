#include <cstdio>
#include <vector>
using namespace std;

int res[2000000];
int startkey[400];
int key[400];
vector<int> keys[400];
int skeys[400];
int rkeys[400];
int n;

bool possible(int status) {
    if (status == 0) return true;
    if (res[status] >= 0) return res[status];
//    printf("Check %d\n", status);
    bool result = false;
    
    for (int i = 0; i < 200; i++) rkeys[i] = startkey[i];
    
    int f = 1;
    for (int i = 0; i < n; i++) {
        if (!(status & f)) {
            for (int j = 0; j < keys[i].size(); j++) {
                rkeys[keys[i][j]]++;
            }
            rkeys[key[i]]--;
        }
        f *= 2;
    }
//    for (int i = 0; i < 10; i++) printf("%d ", rkeys[i]); puts("");
    
    vector<int> next;
    f = 1;
    for (int i = 0; i < n; i++) {
        if ((status & f) && rkeys[key[i]] > 0) {
            next.push_back(f);
        }
        f *= 2;
    }
//    printf("%d: ", (int)next.size());
//    for (int i = 0; i < next.size(); i++) printf("%d ", next[i]); puts("");
    
    for (int i = 0; i < next.size(); i++) {
        if (possible(status ^ next[i])) {
            result = true;
            break;
        }
    }
    
    return res[status] = (result ? 1 : 0);
}

void test() {
    for (int i = 0; i < 2000000; i++) res[i] = -1;
    for (int i = 0; i < 400; i++) startkey[i] = skeys[i] = 0;
    
    int k;
    scanf("%d%d", &k, &n);
    for (int i = 0; i < k; i++) {
        int x; scanf("%d", &x);
        startkey[x-1]++;
        skeys[x-1]++;
    }
    
    int mask = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &key[i], &k);
        key[i]--;
        keys[i].clear();
        for (int j = 0; j < k; j++) {
            int x; scanf("%d", &x);
            keys[i].push_back(x-1);
        }
        mask = 2*mask + 1;
    }
    
    if (!possible(mask)) {
        puts("IMPOSSIBLE");
        return;
    }
    
    for (int i = 0; i < n; i++) {
        
        int sm = 1;
        for (int j = 0; j < n; j++) {
            if (mask & sm && skeys[key[j]] > 0) {
                int nm = mask ^ sm;
                if (possible(nm)) {
                    mask = nm;
                    printf("%d ", j+1);
                    for (int k = 0; k < keys[j].size(); k++) skeys[keys[j][k]]++;
                    skeys[key[j]]--;
                    break;
                }
            }
            sm *= 2;
        }
        
    }
    puts("");
    
}

int main() {
    int t; scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i+1);
        test();
    }
    return 0;
}