#include<bits/stdc++.h>
using namespace std;
inline int calcMask(long long n){
    int ret=0;
    while(n){
        ret|=(1<<(n%10));
        n/=10;
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        long long n;
        cin>>n;
        int mask=0;
        bool f=1;
        for(long long i=1;i<=1000;i++){
            mask|=calcMask(i*n);
            if(mask==(0x3ff)){
                cout<<"Case #"<<z<<": "<<i*n<<"\n";
                f=0;
                break;
            }
        }
        if(f)cout<<"Case #"<<z<<": INSOMNIA\n";
    }
    return 0;
}
