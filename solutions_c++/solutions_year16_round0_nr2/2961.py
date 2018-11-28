#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
typedef pair<int,int> PII;
typedef pair<int,pair<int,int> > PIII;
typedef pair<ll,ll> PLL;

int main(void) {
    int n;
    cin>>n;
    FOR(i,0,n) {
        string s;
        cin>>s;
        int len = s.size(), ans=0;
        for (int j=len-1; j>=0; j--) {
            if (s[j]=='-') {
                ans++;
                for (int k=0; k<=j; k++) {
                    s[k] = (s[k]=='-'?'+':'-');
                }
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
    }
    return 0;
}
