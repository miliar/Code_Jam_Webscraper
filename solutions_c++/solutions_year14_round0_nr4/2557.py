#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    double ans[1001],bns[1001];
    int t,k,n;
    cin>>t;
    for(int k=1; k<=t; k++){
        cin>>n;
        for(int i=0; i<n; i++)cin>>ans[i];
        for(int i=0; i<n; i++)cin>>bns[i];
        sort(ans, ans+n);
        sort(bns, bns+n);
        //Ô­Ê¼
        int p1 = 0;
        for(int i=0; i<n; i++){
            if(bns[i] > ans[p1]){
                p1 ++;
            }
        }
        //for(int i=0; i<n; i++)cout<<ans[i]<<" ";cout<<endl;
        //for(int i=0; i<n; i++)cout<<bns[i]<<" ";cout<<endl;
        //½ø½×
        int p2 = 0;
        for(int i=0; i<n; i++){
            if(ans[i] > bns[p2]){
                p2 ++;
            }
        }
        cout<<"Case #"<<k<<": ";
        cout<<p2<<" "<<n-p1<<endl;
    }
}
