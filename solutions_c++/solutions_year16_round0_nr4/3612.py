#include <iostream>

using namespace std;

int main()
{
    int t,K,C,S;
    cin>>t;
    for(int T=1;T<=t;T++) {
        cin>>K>>C>>S;
        cout<<"Case #"<<T<<":";
        for (int i=1; i <= S; i++) {
            cout<<" "<<i;
        }
        cout<<"\n";
    }
}
