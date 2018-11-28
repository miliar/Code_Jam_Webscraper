#include <iostream>
#include <algorithm>
using namespace std;
int n;
int a[10002],b[10002];
int work(int m){
    int i,j,s=0;
    for(i=1;i<=n;i++) b[i]=a[i];
    for(i=m;i>=1;i--){
        for(j=1;j<i;j++){
            if(b[j]>b[j+1]){
                int t=b[j];
                b[j]=b[j+1];
                b[j+1]=t;
                s++;
            }
        }
    }
    for(i=n;i>m;i--){
        for(j=m+1;j<i;j++){
            if(b[j]<b[j+1]){
                int t=b[j];
                b[j]=b[j+1];
                b[j+1]=t;
                s++;
            }
        }
    }
    return s;
}
void init(){
    int i,minn=1e8,s;
    cin>>n;
    for(i=1;i<=n;i++){
        cin>>a[i];
    }
    for(i=1;i<=n;i++){
        s=work(i);
        if(s<minn) minn=s;
    }
    cout<<minn<<endl;
}
int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int T,C;
    cin>>T;
    for(C=1;C<=T;C++){
        cout<<"Case #"<<C<<": ";
        init();
    }
}