#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t,n,x;
    cin>>t;
    int cases = 1;
    while(t--){
        cin>>n;
        cout<<"Case #"<<cases<<": ";
        int m[n];
        cin>>m[0];
        int res1 = 0;
        int res2 = 0;
        int maxr = 0;
        for(int i = 1;i<n;i++){
            cin>>m[i];
            x = m[i-1]-m[i];
            if(x>0)
                res1 += x;
            maxr = max(maxr,x);
        }
        for(int i = 0;i<n-1;i++){
            if(m[i]<=maxr)
                res2+=m[i];
            else
                res2+=maxr;
        }
        cout<<res1<<" "<<res2<<endl;
    }
    return 0;
}
