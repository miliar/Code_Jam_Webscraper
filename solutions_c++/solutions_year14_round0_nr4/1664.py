#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

double a[1111],b[1111];
int n;

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>n;
        for(int i=0;i<n;i++) cin>>a[i];
        for(int i=0;i<n;i++) cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        int ans1=0;
        int p=0,q=n-1;
        for(int i=0;i<n;i++) {
            if (a[i]>b[p]) {
                ans1++; p++;
            } 
        }
        int ans2=0;
        p=0;
        for(int i=0;i<n;i++) {
            ans2++;
            for(int j=p;j<n;j++) if (b[j]>a[i]) {
                ans2--;
                p=j+1;
                break;
            }
        }
        
        cout<<"Case #"<<T<<": ";
        cout<<ans1<<' '<<ans2;
        cout<<endl;
    }
    return 0;
}