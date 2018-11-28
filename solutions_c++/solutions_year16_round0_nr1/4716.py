#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long n;
    cin>>n;
    int a[10]={0};

    if (n!= 0) {
        for(long long i=1 ; i< 1e6 ; i++) {
            long long p = n*i;
            while (p) {
                a[p%10] = 1;
                p/=10;
            }
            int s = 0;
            for(int j=0 ; j< 10 ; j++) {
                s+= a[j];
            }
            if (s>=10) {
                cout<<n*i<<endl;
                return;
            }

        }
    }

    cout<<"INSOMNIA\n";
}

int main(int argc, const char **argv) {
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; t++) {
        cout<<"Case #"<<t<<": ";
        cerr<<"FINISHED"<<" "<<t<<" "<<endl;
        solve();
    }
}
