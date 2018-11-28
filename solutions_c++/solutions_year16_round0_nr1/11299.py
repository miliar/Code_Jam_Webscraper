/***************************/
/*                         */
/* Coded By: Ankush Sharma */
/*                         */
/***************************/

#include<bits/stdc++.h>
using namespace std;
#define ll long long
set<int> s;

void solve(ll a)
{
    ll temp = a;
    while(temp){

        s.insert(temp%10);
        temp /= 10;
    }
}


int main() {

    std::ios_base::sync_with_stdio(false);

    ifstream fin("input.in");
    ofstream fout("output.out");

    int t, test; fin>>t;
    test = t;

    while(test--) {

        s.clear();
        ll a, ans; fin>> a;
        if(a == 0) { fout<<"Case #"<< t-test<<": INSOMNIA\n"; continue; }
        solve(a);
        for(ll i = 2; s.size() < 10 ; i++) {
            ans = a*i;
            solve(ans);
        }

        fout<<"Case #"<< t-test<<": "<<ans<<"\n";

    }


    return 0;
}
