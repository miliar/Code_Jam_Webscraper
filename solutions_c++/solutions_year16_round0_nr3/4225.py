#include <iostream>
#include <set>
#include <cstdio>
using namespace std;
long long prime(long long x) {
    for(long long i = 2; i * i <= x; ++i) {
        if(x %i == 0) return i;
    }
    return 0;
}
bool next_perm(int*a, int l) {
    for(int i = l-2; i > 0; i--) {
        if(a[i] == 0) {
            a[i] = 1;
            return true;
        }
        a[i] = 0;
    }
    return false;
}
long long base_k(int* a, int l, int k) {
    long long t = 1;
    long long ans = 0;
    for(int i = l-1; i >= 0; --i) {
        ans += t * a[i];
        t *= 1ll * k;
    }
    return ans;
}
int main() {
    int l,n;
    cin>>n;
    cin>>l>>n;
    cout<<"Case #1:\n";
    int a[30];
    a[0] = 1;
    a[l-1] = 1;
    for(int i = 1; i < l-1; ++i) a[i] = 0;
    long long A[11];
    while(n) {
        bool b = true;
        for(int i = 2; i < 11; ++i ) {
            long long t = base_k(a,l,i);
            A[i] = prime(t);
            if(A[i] == 0){
                b = false;
                break;
            }
        }
        if(b) {
            n--;
            for(int i = 0; i < l ;++ i) {
                cout<<a[i];
            }
            for(int i = 2; i < 11; ++i) {
                cout<<" "<<A[i];
            }
            cout<<endl;
        }
        next_perm(a,l);
    }
    return 0;
}
