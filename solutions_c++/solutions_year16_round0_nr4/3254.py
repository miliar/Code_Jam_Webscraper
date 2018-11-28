#include <iostream>
using namespace std;

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        long long K, C, S; cin>>K>>C>>S;
        
        cout<<"Case #"<<t<<": ";

        for (long long x0=0; x0<K; x0++) {
            long long x = x0;
            for (long long c=1; c<C; c++)
                x = K*x + x0;
            cout<<(x+1)<<" ";
        }
        cout<<endl;
    }
    return 0;
}
