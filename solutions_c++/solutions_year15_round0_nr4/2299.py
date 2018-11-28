#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
bool cmp(int a, int b){
    return a>b;
}
int main() {
    freopen("in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t,x,r,c; cin>>t;
    for(int j=1;j<=t;j++){
        cin>>x>>r>>c;
        int f=0;
        if(x==1)f=1;
        else if((r%x==0&&c%(x-1)==0)||(c%x==0&&r%(x-1)==0)||(c%x==0&&r%x==0))f=1;
        cout<<"Case #"<<j<<": "<<(f==0?"RICHARD":"GABRIEL")<<endl;
    }
    return 0;
}
