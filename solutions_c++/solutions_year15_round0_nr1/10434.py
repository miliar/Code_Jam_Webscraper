#include<iostream>
using namespace std;
int main() {
    int test,i,n, iter=1;
    char x;
    cin>>test;
    while(test--) {
        cin>>n;
        int req = 0, tot = 0, res = 0;
        for(i=0;i<=n;i++) {
            cin>>x;
            if(i>tot && x != '0') {
                res += i-tot;
                tot += i-tot;
            }  
            tot += x-'0';
        }
        cout<<"Case #"<<iter<<": "<<res<<endl;
        iter++;
    }
    //system("pause");
}
