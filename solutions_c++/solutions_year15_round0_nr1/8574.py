#include <bits/stdc++.h>
using namespace std;
int main (){
freopen ("A-large.in","r",stdin);
freopen ("A-large.out","w",stdout);
string s;
int t,n,sum=0,add=0;
cin>>t;
for (int i=1;i<=t;i++){
    cin>>n>>s;
    sum=0;
    add=0;
    for (int j=0;j<=n;j++){
        while(j>sum){
            add+=1;
            sum+=1;
        }
        sum+=(s[j]-'0');
    }
    cout<<"Case #"<<i<<": "<<add<<endl;
}
}
