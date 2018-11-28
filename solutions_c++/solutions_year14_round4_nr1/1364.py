
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream &a, const vector<T> &v) {
    a<< "[";
    if (v.size() >= 1) a<<v[0];
    for (int i=1; i<v.size(); i++) {
        a << ", " << v[i];
    }
    a << "]\n";
    return a;
}

int nfiles, cap;
int files[10005];

int main(int argc, char **argv) {
    int TC;
    cin >> TC;
    rep(tc,TC) {
        cin >> nfiles >> cap;
        rep(i,nfiles) cin >> files[i];
        sort(files,files+nfiles);
        int a=0,b=nfiles-1, ans=0;
        while (a<b) {            
            if ( (files[a] + files[b]) <= cap ) a++;
            b--;
            ans++;
        }
        if (a==b) ans++;
        cout << "Case #" << tc+1 << ": " << ans << endl;
    }
}

