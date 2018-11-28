#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 2100;
const int INF = 1000000000;

struct node {
    long long x, y;
    long long n;
};


int n, m;
long long z[MAXN];
long long on[MAXN], off[MAXN];


int main() {
    int tt;
    cin >> tt;
    for (int ttt = 1; ttt <= tt; ++ttt) {
        cin >> n >> m;
        vector<node> people;
        vector<long long> pos;
        for (int i = 0; i < m; ++i) {
            node p;
            cin >> p.x >> p.y >> p.n;
            pos.push_back(p.x);
            pos.push_back(p.y);
            people.push_back(p);
        }
        sort(pos.begin(), pos.end());
        map<long long, int> discrete;
        map<int, long long> disf;
        int tmp = 0;
        discrete[pos[0]] = tmp++;
        disf[0] = pos[0];
        for (int i = 1; i < pos.size(); ++i) 
         if (pos[i] != pos[i-1]) {
             discrete[pos[i]] = tmp++;
             disf[tmp - 1] = pos[i];
         }
        
        memset(z, 0, sizeof(z));
        int len = 0;
        for (int i = 0; i < people.size(); ++i) {
            for (int j = discrete[people[i].x]; j <= discrete[people[i].y]; ++j) z[j] += people[i].n;
            if (discrete[people[i].y] > len) len = discrete[people[i].y];
            on[discrete[people[i].x]] += people[i].n;
            off[discrete[people[i].y]] += people[i].n;
        }
        
        long long ans = 0;
        
        while (true) {
            bool flag = true;
            long long a = 0;
            int b;
            for (int i = 0; i < n; ++i) 
             if (z[i] > a) {
                 a = z[i];
                 b = i;
                 flag = false;
             }
            if (flag) break;
            int l, r;
            l = r = b;
            while (l > 0 && z[l - 1] == z[b]) --l;
            a = 0;
            if (l > 0 && z[l - 1] > a) a = z[l - 1];
            a = z[b] - a;
            if (a > on[l]) a = on[l];
            r = l;
            while (off[r] == 0) ++r;
            if (a > off[r]) a = off[r];
            for (int i = l; i <= r; ++i) z[i] -= a;
            
            on[l] -= a;
            off[r] -= a;
            
            // Discrete!!!
            ans -= a * (n + n + 1 - (disf[r] - disf[l])) * (disf[r] - disf[l]) / 2;
        }
        
        for (int i = 0; i < people.size(); ++i) 
         ans += people[i].n * (n + n + 1 - (people[i].y - people[i].x)) * 
                                           (people[i].y - people[i].x) / 2;
    
        cout << "Case #" << ttt << ": " << ans << endl;
    }

    return 0;
}
