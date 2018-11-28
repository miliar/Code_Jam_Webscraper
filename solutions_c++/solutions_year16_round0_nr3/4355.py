#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <bitset>
using namespace std;

bitset<32ULL> jc;
bool isprime(unsigned long long n) {
    if (n<=1) return false;
    if (n==2) return true;
    unsigned long long ub=sqrt((double)n);
    for (unsigned long long i=2; i<=ub; ++i)
        if (n%i==0) return false;
    return true;
}
int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        int n, j;
        unsigned long long n2;
        cin>>n>>j;
        n2=1ULL<<n;
        cout<<"Case #"<<tc<<":\n";
        for (unsigned long long i=1;  i<n2; ++i) {
            if (!(i&1<<0) || !(i&(1<<n-1))) continue;
            jc=i;
            bool ok=true;
            vector<unsigned long long> vb(9); int idx=0;
            for (int p=2; p<=10; ++p) {
                unsigned long long b=0;
                for (int k=0; k<n; ++k)
                    if (jc[k]==1)
                        b+=pow(p, (double)k);
                if (isprime(b)) {
                    ok=false;
                    break;
                }
                vb[idx++]=b;
            }
            if (ok) {
                vector<int> d(9); idx=0;
                for (int t=0; t<vb.size(); ++t)
                    for (int k=2; k<vb[t]; ++k)
                        if (vb[t]%k==0) {
                            d[idx++]=k;
                            break;
                        }
                if (idx!=9) continue;
                for (int k=n-1; k>=0; --k)
                    cout<<jc[k];
                cout<<' ';
                for (int k=0; k<d.size(); ++k)
                    cout<<d[k]<<' ';
                cout<<'\n';
                --j;
                if (j==0) break;
            }
        }
    }
    return 0;
}