#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    freopen("in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t; cin>>t;
    for(int j=1;j<=t;j++){
        int n; cin>>n;
        char s[1100]; cin>>s; int a=0, c=0;
        for(int i=0;i<=n;i++){
            if(c<i){
                a+=i-c;
                c=i;
            }
            c+=s[i]-'0';
        }
        cout<<"Case #"<<j<<": "<<a<<endl;
    }
    return 0;
}
