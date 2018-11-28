#include <iostream>
using namespace std;

int main(){
    freopen("readable.out","w",stdout);
    int t,k,c,s;
    cin>>t;
    for (int ca=1;ca<=t;ca++){
        cout<<"Case #"<<ca<<": ";
        cin>>k>>c>>s;
        for (int i=1;i<k;i++) cout<<i<<' ';
        cout<<k<<endl;
    }
}