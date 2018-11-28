#include <cstdio>
#include <set>
#include <map>
#include <vector>

using namespace std;

typedef long long ll;

#define lso(x) (x & (-x))

map<ll, int> bitInt;

struct ChestMask{
    ll a, b, c, d;
    const bool isEmpty(){
        return (a | b | c | d) == 0;
    }
    int lsoRemove(){
        if(d == 0){
            if(c == 0){
                if(b == 0){
                    if(a == 0){
                        return -1;
                    }else{
                        ll bit = lso(a);
                        a -= bit;
                        return bitInt[bit] + 150;
                    }
                }else{
                    ll bit = lso(b);
                    b -= bit;
                    return bitInt[bit] + 100;
                }
            }else{
                ll bit = lso(c);
                c -= bit;
                return bitInt[bit] + 50;
            }
        }else{
            ll bit = lso(d);
            d -= bit;
            return bitInt[bit];
        }
    }
    void flip(int i){
        if(i < 50){
            d |= (1ll << i);
        }else if(i < 100){
            c |= (1ll << (i - 50));
        }else if(i < 150){
            b |= (1ll << (i - 100));
        }else{
            a |= (1ll << (i - 150));
        }
    }
    void flipOff(int i){
        if(i < 50){
            d &= ~(1ll << i);
        }else if(i < 100){
            c &= ~(1ll << (i - 50));
        }else if(i < 150){
            b &= ~(1ll << (i - 100));
        }else{
            a &= ~(1ll << (i - 150));
        }
    }
    ChestMask(const ChestMask& o){
        a = o.a;
        b = o.b;
        c = o.c;
        d = o.d;
    }
    void flipOff(const ChestMask& mask){
        a &= ~mask.a;
        b &= ~mask.b;
        c &= ~mask.c;
        d &= ~mask.d;
    }
    void flipOn(const ChestMask& mask){
        a |= mask.a;
        b |= mask.b;
        c |= mask.c;
        d |= mask.d;
    }
    void conj(const ChestMask& mask){
        a &= mask.a;
        b &= mask.b;
        c &= mask.c;
        d &= mask.d;
    }
    ChestMask(){}
};

int keys[204], chestKeys[204];
vector<int> chestContains[204];
int numChests;
ChestMask keyChests[204];
ChestMask chestLocked;
bool chestLockedBool[204];
int n;

vector<int> hasKey[200];

int solution[204];

int gunlockable[204];
bool visited[204];

vector<int> adj[200];

bool gUnlock(int c){
    if(!chestLockedBool[c])return true;
    if(gunlockable[c] != -1)return gunlockable[c];
    if(visited[c])return false;
    if(gunlockable[c] == -1){
        visited[c] = true;
        if(keys[chestKeys[c]]) return gunlockable[c] = 1;
        for(int i = 0; i < adj[c].size(); i++){
            if(chestLockedBool[c] && gUnlock(adj[c][i])){
                return gunlockable[c] = 1;
            }
        }
        return gunlockable[c] = 0;
    }
    return gunlockable[c];
}

bool unlockAll(const ChestMask& unlockables){
    // printf("%d %d\n", numChests, n);
    if(numChests == n){
        return true;
    }
    for(int i = 0; i < n; i++){
        gunlockable[i] = -1;
        visited[i] = false;
    }
    for(int i = 0; i < n; i++){
        if(!gUnlock(i)){
            // printf("%d %d\n", numChests, i);
            return false;
        }
    }
    ChestMask mask = unlockables;
    if(mask.isEmpty())return false;
    ChestMask nm;
    int p;
    while((p = mask.lsoRemove()) != -1){
        int k = chestKeys[p];
        nm = unlockables;
        keys[k]--;
        solution[numChests] = p;
        numChests++;
        chestLocked.flipOff(p);
        chestLockedBool[p] = false;
        for(int i = 0; i < chestContains[p].size(); i++){
            int kk = chestContains[p][i];
            if(keys[kk] == 0){
                nm.flipOn(keyChests[kk]);
            }
            keys[kk]++;
        }
        if(!keys[k]){
            nm.flipOff(keyChests[k]);
        }
        nm.conj(chestLocked);
        if(unlockAll(nm)){
            return true;
        }
        for(int i = 0; i < chestContains[p].size(); i++){
            int kk = chestContains[p][i];
            keys[kk]--;
        }
        chestLocked.flip(p);
        chestLockedBool[p] = true;
        keys[k]++;
        numChests--;
    }
    return false;
}

int main(){
    int t;
    scanf("%d\n", &t);
    ChestMask empty;
    empty.a = empty.b = empty.c = empty.d = 0;
    ChestMask ini;
    int ca = 1;
    for(int i = 0; i < 52; i++){
        bitInt[1ll<<i] = i;
    }
    int keysNeeded[204];
    while(t--){
        int k;
        scanf("%d %d\n", &k, &n);
        // printf("%d %d\n", k, n);
        memset(keys, 0, sizeof(keys));
        memset(keysNeeded, 0, sizeof(keysNeeded));
        for(int i = 0; i < 200; i++){
            keyChests[i] = empty;
            hasKey[i].clear();
        }
        chestLocked = empty;
        ini = empty;
        int kk;
        while(k--){
            scanf("%d\n", &kk);
            kk--;
            keys[kk]++;
            keysNeeded[kk]--;
        }
        for(int i = 0; i < n; i++){
            chestLocked.flip(i);
            chestLockedBool[i] = true;
            int tt;
            scanf("%d\n", &tt);
            tt--;
            chestKeys[i] = tt;
            keyChests[tt].flip(i);
            keysNeeded[tt]++;
            if(keys[tt]){
                ini.flip(i);
            }
            scanf("%d\n", &tt);
            chestContains[i].clear();
            while(tt--){
                int kk;
                scanf("%d\n", &kk);
                kk--;
                chestContains[i].push_back(kk);
                keysNeeded[kk]--;
                hasKey[kk].push_back(i);
            }
        }
        for(int i = 0; i < n; i++){
            int k = chestKeys[i];
            adj[i].clear();
            for(int j = 0; j < hasKey[k].size(); j++){
                adj[i].push_back(hasKey[k][j]);
            }
        }
        numChests = 0;
        printf("Case #%d:", ca++);
        bool possible = true;
        for(int i = 0; i < 204; i++){
            if(keysNeeded[i] > 0){
                // printf("%d %d\n", i, keysNeeded[i]);
                possible = false;
                break;
            }
        }
        if(possible && unlockAll(ini)){
            for(int i = 0; i < n; i++){
                printf(" %d", solution[i] + 1);
            }
            printf("\n");
        }else{
            printf(" IMPOSSIBLE\n");
        }
    }
}