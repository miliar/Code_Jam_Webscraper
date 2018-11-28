#include<bits/stdc++.h>

using namespace std;

typedef long long llong;
llong powe(llong base,llong index) {
    if(!index)
        return 1;
    llong temp=powe(base,index>>1);
    temp*=temp;
    if(index&1)
        temp*=base;
    return temp;
}
int main() {

    freopen("C:\\Users\\Saurabh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh\\Desktop\\out.txt","w",stdout);

    int t,cas=1;
    cin>>t;
    while(t--) {
        int k,c,s,i;
        cin>>k>>c>>s;
        llong ind=1,power=powe(k,c-1);
        cout<<"Case #"<<cas++<<": ";
        for(i=0;i<k;i++) {
            cout<<ind<<" ";
            ind+=power;
        }
        cout<<endl;
    }

    return 0;
}
