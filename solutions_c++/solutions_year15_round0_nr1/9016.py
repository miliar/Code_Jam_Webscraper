#include<bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define all(x)      (x).begin(), (x).end()
#define re(i,s,n)   for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef unsigned long long ull;
template<class T> T gcd(T a, T b) {
    return b ? gcd(b, a % b) : a;
}
const double EPS = 1e-7;

int main() {
    int t;
    cin >> t;
    for(int test=1; test<=t; test++) {
        int s;
        cin >> s;

        string cnt;
        cin >> cnt;
        int standing = 0;
        int ans = 0;
        fr(i,s+1) {
            if(cnt[i]-'0'>0) {
                if(standing >= i) {
                    standing += cnt[i] - '0';
                } else {
                    ans += i - standing;
                    standing += i - standing + (cnt[i] - '0');
                }
            }
        }

        cout << "Case #"<< test <<": " << ans << endl;
    }


    return 0;
}


