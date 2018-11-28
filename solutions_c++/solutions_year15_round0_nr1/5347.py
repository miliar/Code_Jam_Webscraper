#include<iostream>

using namespace std;

char str [1003];
int main () {

    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    int smax;
    int sofar_stood,invites;
    for (int j=1;j<=t;j++) {
        cin>>smax;
        cin>>str;
        invites=0;
        sofar_stood=str[0]-'0';

        for (int i=1;i<=smax;i++) {
            if (str[i]>'0'&&sofar_stood<i) {
                invites += i-sofar_stood;
                sofar_stood +=invites;
            }
            sofar_stood += str[i]-'0';
        }
        cout<<"Case #"<<j<<":  "<<invites<<endl;

    }
    return 0;
}
