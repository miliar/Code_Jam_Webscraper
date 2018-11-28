#include <iostream>
#include <list>
#include <vector>
#include <string>

using namespace std;

int main() {
    int T, n, i, cnt, pi;
    int K, C, S;

    cin>>T;

    cnt=1;
    for (; cnt<=T; ++cnt) {
        cin>>K>>C>>S;
        
        cout<<"Case #"<<cnt<<":";
        if (C == 1) {
            if (S < K) {
                cout<<" IMPOSSIBLE";
            } else {
                for (i=1; i<=K; ++i) {
                    cout<<" "<<i;
                }
            }
        } else {
            if (K == 1) {
                if (S < 1) {
                    cout<<" IMPOSSIBLE";
                } else {
                    cout<<" 1";
                }
            } else if (K == 2) {
                if (S < 1) {
                    cout<<" IMPOSSIBLE";
                } else {
                    cout<<" 2";
                }
            }
            else if (K == 3) {
                if (S < 2) {
                    cout<<" IMPOSSIBLE";
                } else {
                    cout<<" 2 6";
                }
            } else {
                if (S < (K-2)){
                    cout<<" IMPOSSIBLE";
                } else {
                    for (i=2; i<K-1; ++i) {
                        cout<<" "<<i;
                    }
                    cout<<" "<<(K * (K-1));
                }
            
            }
        }
        cout<<"\n";

    }
    
    return 0;
}

