#include <bits/stdc++.h>
using namespace std;
//make_tuple emplace_back next_permutation push_back make_pair second first setprecision

#if MYDEBUG
#include "lib/cp_debug.h"
#else
#define DBG(...) ;
#endif

using LL = long long;
constexpr LL LINF=334ll<<53;
constexpr int INF=15<<26;
constexpr LL  MOD=1E9+7;

struct Problem{
    int k;
    string s;

    void solve(){
        cin >> s >> k;
        int ans =0;
        vector<int> im(s.length()+2),flipped(s.length()+1),st(s.length()+1);
        for(int i=1; i<=s.length()-k+1; ++i){
            st[i]=(s[i-1]=='+'?1:0);
            flipped[i]=flipped[i-1]^im[i];
            DBG(i,s.length(),st[i],flipped[i])
            if(!(st[i]^flipped[i])){
                flipped[i]=!flipped[i];
                im[i+k]=1;
                ans++;
            }
        }
        for(int i=s.length()-k+2; i<=s.length(); ++i){
            DBG(i,s.length())
            st[i]=(s[i-1]=='+'?1:0);
            flipped[i]=flipped[i-1]^im[i];
            if(!(st[i]^flipped[i])){
                cout << "IMPOSSIBLE"<<"\n";
                return;
            }
        }
        cout << ans <<"\n";
    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ": ";
        Problem p;
        p.solve();
    }

    return 0;
}

