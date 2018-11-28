#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool myfunc(pair<char, int> a, pair<char, int> b) {
    return (a.second>b.second);
}

int main() {

    ll t, n, m, i, j, k, a, b, x;
    cin>>t;
    ll tt = t;
    vector<pair<char, int> > u, v;
    while(t--) {
        v.clear();
        cin>>n;
        m = 0;
        v.resize(n);
        for (i=0; i<n; i++) {
            v[i].first = 'A' + i;
            cin>>v[i].second;
            m += v[i].second;
        }
        u = v;
        sort(u.begin(), u.end(), myfunc);
        cout<<"Case #"<<(tt-t)<<":";
        while(u[0].second!=0) {
            if (u[1].second*2 > (m-1)) {
                cout<<" "<<u[0].first<<u[1].first;
                u[0].second--;
                u[1].second--;
                m = m-2;
            }
            else {
                cout<<" "<<u[0].first;
                u[0].second--;
                m--;
            }
            sort(u.begin(), u.end(), myfunc);
            //cout<<m<<u[0].second<<u[1].second<<endl;
        }
        cout<<endl;

    }


    return 0;

}