#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define fst first
#define snd second
#define fr(i, a, b) for(int i=a; i<b; i++)

ll solve(int a, int b) {
    ll res = 1;
    ll base = b;
    for(int i=0; i<=13; i++) {
        res += ((a>>i)&1) * base;
        base *= b;
    }
    res += base;
    return res;
}
void main2() {
    int n, j;
    cin>>n>>j;
    vector<ll> res;
    res.clear();
    int s = (1<<14);
    int cnt = 0;
    for(int i=0; i<s; i++) {
        res.clear();
        for(int base = 2; base<=10; base++) {
            ll temp = solve(i, base);
            bool ok = false;
            for(ll j=2; j*j<=temp; j++) {
                if(temp % j ==0) {
                    //cout<<"temp: "<<temp<<" j:"<<j<<endl;
                    res.push_back(j); ok = true; break;
                }

            }
            if(!ok) {res.clear(); break;}
        }
        if(res.size()==9) {
            cnt++;
            cout<<"1";
            for(int j=13; j>=0; j--)
                if((i>>j)&1) cout<<"1";
                else cout<<"0";
            cout<<"1";
            for(int j=2; j<=10; j++) {
                cout<<" "<<res[j-2];
            }
            cout<<endl;
        }
        if(cnt == 50) break;
    }

}

int main() {
    int T;
    cin>>T;
    for(int i=1; i<=T; i++) {
        cout<<"Case #"<<i<<":"<<endl;
        main2();
    }
}
