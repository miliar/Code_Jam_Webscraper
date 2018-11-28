#include<iostream>
#include<windows.h>
using namespace std;

long long dopot(int k, int c) {
    long long w = 1;
    for(int i = 1; i<=c; i++)
        w*=k;
    return w;
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        int K, C, S;
        cin>>K>>C>>S;
        cout<<"Case #"<<tt<<": ";

        for(int i=1; i<=K; i++)
            cout<<i<<" ";
        cout<<endl;
    }
    return 0;
}
