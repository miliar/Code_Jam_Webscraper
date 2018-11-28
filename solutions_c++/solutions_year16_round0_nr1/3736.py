#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("ALarge.out","w",stdout);
    int T;
    ll n;
    cin >> T;
    int cases = 0;
    set<ll>  visit;
    set<int> digits;
    while(T--){
        cases++;
        cin >> n;
        visit.clear();
        digits.clear();
        ll i = 1LL;
        ll aux = n;

        while( digits.size() < 10 ){
            aux = i * n;
//            cout << aux << endl;
            if( visit.count(aux) ) break;
            visit.insert(aux);
            ll lel = aux;
            while( lel > 0 ){
                digits.insert(lel%10);
                lel = lel / 10;
            }
            i++;
        }

        cout << "Case #" << cases << ": ";
        if( digits.size() == 10 ) cout << aux << endl;
        else cout << "INSOMNIA" << endl;
    }
}
