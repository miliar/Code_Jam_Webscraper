#include <bits/stdc++.h>
#include "InfInt.h"
using namespace std;



int main() {
    int T;
    scanf("%d", &T);
    for(int z=1;z<T+1;++z) {
        int n,j;
        cin >> n >> j;
        InfInt v[11];
        int cnt=0;
        cout << "Case #" << z << ":" << "\n";
        for(long long i=(1LL<<31)+1LL;i<(1LL<<32)-1LL;i+=2LL){
            bool ok=true;
            int msb=64-__builtin_clzll(i);
            if(msb!=n)
                continue;
            for(int base=2;base<=10;++base){
                InfInt m = 0LL,pow=1LL;
                for(int k=0;k<msb;++k){
                    if((i&(1<<k)))
                        m+=pow;
                    pow*=base;
                }
                bool found=false;
                for(InfInt k=2LL;k*k<=m;++k){
                    if(m%k==0){
                        v[base]=k;
                        found = true;
                        break;
                    }
                    if(k==1000LL){
                        break;
                    }
                }
                if(!found){
                    ok = false;
                    break;
                }
                if(base==10){
                    v[1]=m;
                }
            }
            if(ok){
                cnt++;
                cout << v[1] << " ";
                for(int k=2;k<=10;++k){
                    cout << v[k] << " ";
                }
                cout << endl;
            }
            if(cnt==j)
                break;
        }
    }
    return 0;
}
