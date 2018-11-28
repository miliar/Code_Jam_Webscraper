#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl

using namespace std;
using namespace tr1;

typedef pair<string, int> Pair;

int t, n;
vector <int> ar;
queue <vector <int> > Q;
unordered_map <unsigned long long int, int> mp;
const unsigned long long int base = 1000000007ULL;

unsigned long long int getHash(vector <int> v){
    int i;
    unsigned long long int h = 0;
    for (i = 0; i < n; i++) h = (h * base) + v[i];
    return h;
}

bool F(vector <int> v){
    int idx = 0, mx = v[0];
    for (int i = 0; i < n; i++){
        if (v[i] > mx) mx = v[i], idx = i;
    }

    for (int i = 0; i < idx; i++){
        if (v[i] > v[i + 1]) return false;
    }

    for (int i = idx + 1; i < n; i++){
        if (v[i] > v[i - 1]) return false;
    }

    return true;
}

int bfs(){
    if (F(ar)) return 0;

    mp.clear();
    while (!Q.empty()) Q.pop();

    mp[getHash(ar)] = 1;
    Q.push(ar);
    while (!Q.empty()){
        vector <int> v = Q.front();
        Q.pop();

        int dis = mp[getHash(v)];
        for (int i = 0; (i + 1) < n; i++){
            swap(v[i], v[i + 1]);
            unsigned long long int h = getHash(v);
            if (!mp[h]){
                mp[h] = dis + 1;
                Q.push(v);
                if (F(v)) return (mp[getHash(v)] - 1);
            }
            swap(v[i], v[i + 1]);
        }
    }

    return -1;
}

int main(){
    read();
    write();
    int T = 0, i, j, k;

    scanf("%d", &t);
    while (t--){
        ar.clear();
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%d", &k);
            ar.push_back(k);
        }

        int res = bfs();
        printf("Case #%d: %d\n", ++T, res);
    }
    return 0;
}
