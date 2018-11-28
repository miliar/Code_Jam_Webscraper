#include <bits/stdc++.h>

using namespace std;
typedef long long LL;

int main()
{
    ifstream cin("fractiles.in");
    ofstream cout("fractiles.out");
    LL t; cin >> t;
    for(LL q = 0;q<t;q++){
        LL k,c,s; cin >> k >> c >> s;
        cout << "Case #" << (q+1) << ": ";
        if(s*c < k){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        for(LL j = 0;j<k;j+=c){
            LL ind = 0;
            for(LL i = j;i<k && i<j+c;i++)
                ind = k*ind + i;
            cout << (ind+1) << " ";
        }
        cout << "\n";
    }
    return 0;
}
