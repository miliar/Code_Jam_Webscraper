#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int main(){
    freopen("gold.in","r",stdin);
    freopen("gold.out","w",stdout
            );
    int t,i,j,k,c,s;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<": ";
        for(j=1;j<=s;j++)
            cout<<j<<" ";
        cout<<endl;
    }
    return 0;
}
