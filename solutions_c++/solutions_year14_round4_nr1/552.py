#include <iostream>
#include <algorithm>
using namespace std;
int n,m;
int a[10002];
void init(){
    int i;
    cin>>n>>m;
    for(i=1;i<=n;i++){
        cin>>a[i];
    }
    sort(a+1,a+1+n);
    int l=1,r=n,s=0;
    while(l<=r){
        if(a[l]+a[r]<=m){
            l++;
            r--;
        }
        else r--;
        s++;
    }
    cout<<s<<endl;
}
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,C;
    cin>>T;
    for(C=1;C<=T;C++){
        cout<<"Case #"<<C<<": ";
        init();
    }
}