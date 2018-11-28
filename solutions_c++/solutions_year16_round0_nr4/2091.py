#include<iostream>
#include<cstdint>
#define LL uint64_t
using namespace std;

void c() {
    LL k,c,s;
    cin>>k>>c>>s;
    for(LL i=0;i<k;i++) {
        LL tot=0;
        LL pow=1;
        for(LL p = 0; p < c;p++) {
            tot += i * pow;
            pow *= k;
        }
        cout<<tot+1<<" ";
    }
    cout<<endl;
}


int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {cout<<"Case #"<<i<<": ";c();}

}
