#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll eval(int mask, int b) {
    ll p = 1;
    ll ans = 0;

    for(int i = 0; (1 << i) <= mask; ++i) {
        if((1 << i) & mask)
            ans += p;
        p = p * b;
    }

    return ans;
}

ll getDivisor(ll mask, int b) {
    
    for(int d = 2; d <= 20; ++d) {
        int r = 0, p = 1;
        for(ll i = 0; (1LL << i) <= mask; ++i) {
            if((1LL << i) & mask)
                r = (r + p) % d;
            p = p * b % d;
        }

        if(r == 0)
            return d;
    }

    return -1;
}

int main() {
    
    srand(time(0));

    ifstream cin("testClarge.in");
    ofstream cout("testClarge.out");
    
    cout << "Case #1:\n";
    
    ll full = (1LL << 31) + 1;
    int cnt = 0;
    set<ll> S;
    int trials = 0;

    do {
        trials++;
        ll temp = full;
        for(int i = 1; i <= 30; ++i)
            if(rand() % 2 == 1)
                temp += (1LL << i);
        
        if(S.find(temp) != S.end())
            continue;

        bool ok = true;
        vector<int> sol;

        for(int b = 2; b <= 10; ++b) {
            int d = getDivisor(temp, b);
            if(d == -1) {
                ok = false;
                break;
            }
            sol.push_back(d);
        }
        
        if(!ok)
            continue;

        for(ll i = 31; i >= 0; --i)
            if(temp & (1LL << i))
                cout << "1";
            else
                cout << "0";

        for(auto temp : sol)
            cout << " " << temp;
        cout << "\n";
        
        S.insert(temp);

        ++cnt;
        cerr << cnt << "\n";
        if(cnt == 500)
            break;
    } while(1);
    cerr << trials << "\n";
}
