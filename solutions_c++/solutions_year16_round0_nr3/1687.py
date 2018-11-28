#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int T;
    cin>>T;
    for (int i=1;i<=T;i++) {
        int k,c,s;
        cin>>k>>c>>s;
        cout << "Case #" << i << ": ";
        unsigned long tile = 1;
        unsigned long acc = pow(k,c-1);
        for (int i=1;i<k;i++) {
            cout<<tile<<" ";
            tile += acc;
        }
        cout<<k<<endl;
    }
}