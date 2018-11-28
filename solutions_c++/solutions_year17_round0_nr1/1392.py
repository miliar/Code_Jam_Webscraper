//This template was originally written by zscoder and copied by duckmoon.
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key
#define INF 2e18

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector< pair<ll, ll> > vii;
typedef vector<int> vi;
typedef long double ld;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

int t, k, ans;
bool pos;
string s;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for(int x = 1; x <= t; x++){
        cin >> s >> k;
        ans = 0;
        for(int i = 0; i <= s.size()-k; i++){
            if(s[i] == '-'){
                for(int j = 0; j < k; j++){
                    if(s[i+j] == '+'){
                        s[i+j] = '-';
                    }
                    else{
                        s[i+j] = '+';
                    }
                }
                ans++;
            }
        }
        pos = 1;
        for(int i = 0; i < k; i++){
            if(s[s.size()-1-i] == '-'){
                pos = 0;
                i = k;
            }
        }
        if(pos){
            cout << "Case #" << x << ": " << ans << endl;
        }
        else{
            cout << "Case #" << x << ": IMPOSSIBLE\n";
        }
    }
}
