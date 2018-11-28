#include<bits/stdc++.h>
using namespace std;
#define ll long long
template<class T> void debug(T v) {
    for(int i=0;i<(int)v.size();i++)cout << v[i] <<" ";cout<<endl;
}
template<class T> void input(T &v) {
    for(int i=0;i<(int)v.size();i++)cin>>v[i];
}

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t;
    cin >> t;
    for(int cs = 1; cs <= t; cs++) {
        long long n, m;
        cin >> n;
        printf("Case #%d: ", cs);
        if(n==0) {
            cout << "INSOMNIA\n";
            continue;
        }
        set<int>s;
        int i;
        for( i=1;;i++) {
            m = n*i;
            while(m) {
                s.insert(m%10);
                m/=10;
            }
            if(s.size()==10)break;
        }
        cout << n*i <<endl;
    }

    return 0;
}

