#include <iostream>
#include <map>
using namespace std;
int f[(1 << 20) + 5], n, k;
int type[555];
int init_keys[555], get_keys[555][555];
int total_keys[(1 << 20) + 5][223];
int consume_keys[(1 << 20) + 5][233];

int dp(int mask) {
    if(f[mask] != -1) return f[mask];
    if(mask == (1 << n) - 1) return f[mask] = 1;

    int ret = 0;
    for(int i = 0; i < n; i++) if(!(mask & (1 << i))) 
        if(init_keys[type[i]] + total_keys[mask][type[i]] - consume_keys[mask][type[i]] > 0) ret |= dp(mask ^ (1 << i));
    
    return f[mask] = ret;
}

void dp1(int mask) {
    if(mask == (1 << n) - 1) return;

    int ret = 0;
    for(int i = 0; i < n; i++) if(!(mask & (1 << i))) 
        if(init_keys[type[i]] + total_keys[mask][type[i]] - consume_keys[mask][type[i]] > 0) {
            if(dp(mask | (1 << i))) {
                cout << i + 1 << " ";
                dp1(mask | (1 << i));
                break;
            }
        }
}

void run() {
    int tmp, c;
    memset(type, 0, sizeof(type));
    memset(init_keys, 0, sizeof(init_keys));
    memset(get_keys, 0, sizeof(get_keys));
    memset(total_keys, 0, sizeof(total_keys));
    memset(consume_keys, 0, sizeof(consume_keys));
    memset(f, -1, sizeof(f));

    cin >> k >> n;
    for(int i = 0; i < k; i++) { cin >> tmp; init_keys[tmp] ++; }
    for(int i = 0; i < n; i++) {
        cin >> type[i] >> c;
        for(int mask = 0; mask < (1 << n); mask ++) if(mask & (1 << i)) consume_keys[mask][type[i]] ++;
        for(int j = 0; j < c; j++) { 
            cin >> tmp; get_keys[i][tmp]++; 
            for(int mask = 0; mask < (1 << n); mask ++) if(mask & (1 << i)) total_keys[mask][tmp] ++;
        }
    } 

    int ret = dp(0);

    if(!ret) cout << "IMPOSSIBLE" << endl;
    else { dp1(0); cout << endl;}
}

int main() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        run();
    }
    return 0;
}
