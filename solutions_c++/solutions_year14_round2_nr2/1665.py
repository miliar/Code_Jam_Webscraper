#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;


int solve() {
    int a, b, k;
    cin>>a>>b>>k;
    int res =0LL;
    for(int i=0; i<a; ++i)
        for(int j=0; j<b; ++j)
            if((i&j) < k) res++;

    return res;
}

int main(){
    ios_base::sync_with_stdio(0);
    int testy;
    cin>>testy;
    for(int i=1; i<=testy; ++i)
    {
        int ans = solve();
        cout<<"Case #"<<i<<": ";
        cout<<ans;
        cout<<"\n";
    }
    return 0;
}
