#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
typedef pair<int,int> PII;
typedef pair<int,pair<int,int> > PIII;
typedef pair<ll,ll> PLL;

int main(void) {
    int T;
    cin>>T;
    FOR(t,0,T){
        int K,C,S;
        cin>>K>>C>>S;
        cout<<"Case #"<<(t+1)<<":";
        for(int i=1;i<=S;i++){
            cout<<" "<<i;
        }
        cout<<endl;
    }
    return 0;
}
