#define OSW2

#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;



int main() {
#ifdef OSW
    freopen("//Users//osw//Desktop//in.txt", "r", stdin);
#endif
#ifdef OSW2
    string file_name = "D-small-attempt0";
    freopen(("//Users//osw//Downloads//" + file_name + ".in").c_str(), "r", stdin);
    freopen(("//Users//osw//Downloads//" + file_name + ".out").c_str(), "w", stdout);
#endif
    
    int T, t = 0;
    cin >> T;

    while (T-(t++)) {
        ll n; cin >> n;
        
        map<ll, ll> mp;
        std::vector<ll> vs(n), vc(n);
        for (int i = 0; i < n; ++i) cin >> vs[i]; 
        for (int i = 0; i < n; ++i) cin >> vc[i]; 

        ll sum = 0;
        while (n--) {
            sum += vc[n];
            mp[vs[n]] = vc[n];
        }

        //cout << sum << endl;
        multiset<ll> ans;
        while (mp.size()!=1) {
            ll neg = 0;
            
            auto it = mp.begin();
            if (it->first==0) ++it;
            ll x = it->first;
            ans.insert(x);

            //
            if (x<0) neg = 1;

            if (!neg)
            for (auto p:mp) {
                ll val = p.first;
                ll cnt = p.second;
                if(mp.count(val+x)) mp[val+x] -= cnt;
            }
            else
            for (auto it = mp.rbegin(); it!=mp.rend(); ++it) {
                auto& p = *it;
                ll val = p.first;
                ll cnt = p.second;
                if(mp.count(val+x)) mp[val+x] -= cnt;
            }

            auto mp2 = mp;
            for(auto p:mp) if(p.second == 0) mp2.erase(p.first);
            swap(mp,mp2);
            
            //cout << x << ":  " << endl;
            //for(auto p:mp) cout << p.first << ' '; cout << endl;
            //for(auto p:mp) cout << p.second << ' '; cout << endl;
        }

        int s0 = mp[0];
        while (s0!=1) s0/=2, ans.insert(0);




        cout << "Case #" << t << ": ";
        for(auto x:ans) cout << x << ' '; cout << endl; 
    }
}



