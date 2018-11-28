#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    int t, i, j, sm, s, n, z;
    cin >> t;
    char ch;
    for(j=1;j<=t;j++) {
        z=0;
        s=0;
        n=0;
        cin >> sm;
        char a[sm];
        for(i=0;i<=sm;i++) {
            cin>>a[i];
        }
        for(i=0;i<=sm;i++) {
            z=i-s;
            if(a[i]-48!=0) {
                if(s>=i)
                    s+=a[i]-48;
                else {
                    n+=z;
                    s=s+z+a[i]-48;
                }
            }
        }
        cout<<"Case #"<<j<<": "<<n<<endl;
    }
}
