#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("OUT.txt", "w", stdout);
    int t,s;
    string cad;
    long long x,r;
    cin>>t;
    for(int k=1;k<=t;k++){
        x=0;r=0;
        cin>>s>>cad;
        for(int i=0;i<(s+1);i++){
            if(x<i && cad[i]!='0'){
                r+=i-x;
                x=i;
            }
            x+=cad[i]-'0';
        }
        cout<<"Case #"<<k<<": "<<r<<endl;
    }
    return 0;
}