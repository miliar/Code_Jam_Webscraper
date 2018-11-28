#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n,m;
int a[11111];

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>n>>m;
        for(int i=0;i<n;i++) cin>>a[i];
        sort(a,a+n);
        int ans=0;
        int k=n-1;
        for(int i=0;i<n;i++) {
            if (a[i]==0) continue;
            if (i>=k) {
                ans++;
            } else {
                while ( (k>i) && (a[k]+a[i]>m) ) k--;
                if ((a[i]+a[k]<=m)&&(i<k)) {
                    a[k]=0;
                    k--;
                    a[i]=0;
                    ans++;
                } else {
                    a[i]=0;
                    ans++;
                }
            }
        }
        cout<<"Case #"<<T<<": ";
        cout<<ans;
        cout<<endl;
    }
    return 0;
}