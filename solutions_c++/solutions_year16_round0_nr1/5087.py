#include <iostream>
#include <set>
#include <cstdio>
using namespace std;
int main() {
    freopen("A-small-attempt0.in","r",stdin);
  //  freopen("output.txt","w", stdout);
    int T;
    cin>>T;
    int k = 0;
    while(T--) {
        k++;
        int ans = 1;
        long long n;
        cin>>n;
        set <long long> S;
        bool d[10];
        for(int i =0; i <= 9; ++i) {
            d[i] = false;
        }
        int b = 0;
        while(b<10){
            long long p = n * ans;
  //          cout<<p<<endl;
            if(S.find(p) != S.end() && (!(S.empty())) ) {
                printf("Case #%d: INSOMNIA\n", k);
                break;
            }
            S.insert(n);
            while(p) {
                b += (d[p%10] == false ? 1 : 0);
                d[p%10] = true;
                p/= 10;
                if(b > 9) {
                    printf("Case #%d: %lld\n", k, n*ans);
                    break;
                }
            }
            ans++;
        }
    }
    return 0;
}