#include <iostream>
#include <cmath>

using namespace std;

long long t,k,c,s;

int main(){
    cin>>t;
    for(int x=0;x<t;x++){
        cin>>k>>c>>s;
        cout<<"Case #"<<x+1<<":";
        for(long long i=0;i<s;i++){
            long long z=pow(k,c-1);
            z=z*i+1;
            cout<<" "<<z;
        }
        cout<<endl;
    }
    return 0;
}
