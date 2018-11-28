#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    long long N;
    cin>>T;
    for(int icase = 1; icase <= T; icase++){
        cin>>N;
        if(N == 0) {
            printf("Case #%d: INSOMNIA\n", icase);
            continue;
        }

        map<int, bool> mib;
        long long V = 0, C;
        while(1){
            V += N;
            C = V;
            while(C){
                mib[C%10] = 1;
                C /= 10;
            }
            if(mib.size() == 10) break;
        }
        printf("Case #%d: %lld\n", icase, V);
    }
    return 0;
}
