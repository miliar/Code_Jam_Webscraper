#include <iostream>
using namespace std;

int main() {
    long long int t,dt,i,k,c,s;
    cin>>t;
    dt=t;
    while(t--)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<dt-t<<": ";
        for(i=1;i<=s;i++)
        cout<<i<<" ";
        cout<<endl;
    }
    return 0;
}
