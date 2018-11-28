#include <iostream>
#include <string>
using namespace std;

int a[16],b[16];
int aa,bb;

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>aa;
        for(int i=0;i<16;i++) cin>>a[i];
        cin>>bb;
        for(int i=0;i<16;i++) cin>>b[i];
        int cnt=0,ans=0;
        for(int i=aa*4-4;i<aa*4;i++) for(int j=bb*4-4;j<bb*4;j++)
            if (a[i]==b[j]) {
                cnt++; ans=a[i];
            }
        cout<<"Case #"<<T<<": ";
        if (cnt==0) cout<<"Volunteer cheated!";
        else if (cnt==1) cout<<ans;
        else cout<<"Bad magician!";
        cout<<endl;
    }
    return 0;
}