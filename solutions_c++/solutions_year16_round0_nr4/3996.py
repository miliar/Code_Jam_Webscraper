//codejam 2016 fractiles
#include <iostream>

using namespace std;

int main(){
    int testCase;
    cin>>testCase;
    for (int i=0; i<testCase; i++){
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<i+1<<":";
        for (int j=1; j<=k; j++){
            cout<<" "<<j;
        }
        cout<<endl;
    }
}
