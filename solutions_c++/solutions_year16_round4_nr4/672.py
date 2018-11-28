#include <bits/stdc++.h>
using namespace std;
typedef long long int lint;

int N;

int om;
int M;

bool poss(int i, vector<int> &O, vector<bool> &taken) {
    if(i == N) return true;
    bool found = false;
    for(int j = 0; j < N; j++) {
        if(taken[j]) continue;
        if(M & (1 << (O[i]*N+j))) {
            taken[j] = true;
            if(!poss(i+1, O, taken)) return false;
            taken[j] = false;
            found = true;
        }
    }
    return found;
}

void code() {
    cin >> N;
    om = M = 0;
    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < N; j++) {
            if(s[j] == '1') {
                om |= 1 << (i*N+j);
            }
        }
    }


    int min_cost = INT_MAX;
    for(int m = 0; m < (1 << (N*N)); m++) {
        if(m & om) continue;
    vector<int> O(N);
    for(int i = 0; i < N; i++) {
        O[i] = i;
    }
        int cost = 0;
        M = om | m;
        int mc = m;
        while(mc) {
            cost++;
            mc = mc & (mc-1);
        }
        if(m == 273) {
            m = 273;
        }
        do {
            vector<bool> taken(N, false);
            if(!poss(0, O, taken)) goto next;
        } while(next_permutation(O.begin(), O.end()));
        if(cost < min_cost) {
            min_cost = cost;
        }
next:;
    }
    cout << min_cost;
}

int main() {
    int t;
    cin >> t;
    for(int tt=1; tt<=t; tt++) {
        cout << "Case #" << tt << ": ";
        code();
        cout << endl;
    }
}
