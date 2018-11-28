#include<iostream>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        int K, C, S;
        cin>>K>>C>>S;
        unsigned long long pow = 1;
        for(int i=1;i<C;i++)
            pow *= K;
        cout<<"Case #"<<t<<":";
        for(int i=1;i<=K;i++)
            cout<<" "<<i*pow;
        cout<<endl;
    }
    return 0;
}
