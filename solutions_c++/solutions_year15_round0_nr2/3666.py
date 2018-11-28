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
        vector<int> A(n);
        rep(i,n)
            cin >> A[i];

        int res = 100000;
        For(i, 1, 1001) {
            int cur = i;
            rep(k,n)
                cur += ((A[k] + i-1) / i) - 1;
            res = std::min(res, cur);
        }
        cout<<"Case #"<<(tp+1)<<": "<<res<<endl;
    }
}
