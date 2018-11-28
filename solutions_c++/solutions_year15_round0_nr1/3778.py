#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)


int main() {
    int np; cin>>np;
    rep(tp, np) {
        int n; cin >> n;
        string str; cin>>str;
        int res = 0;
        int acc = 0;
        rep(i,n+1) {
            int cur = str[i] - '0';
            int plus = max(i - acc, 0);
            res += plus;
            acc += plus;
            acc += cur;
        }
        cout<<"Case #"<<(tp+1)<<": "<<res<<endl;

    }
}
