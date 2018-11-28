#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
typedef long long LL;
const int inf=1000000000;//1e9
int main(){
    int T;
    int n;
    LL p;
    LL total;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    cin>> T;
    for (int t=1;t<=T;t++){
        cin>>n>>p;
        total = 1LL << n;
        p--;
        int w=0;
        while ((1LL<<(n-w))-1>p) w++;
        LL ans2=total - (1LL<<w);
        int L =n;
        while (total-(1LL<<(n-L))>p) L--;
        cerr<<L<<endl;
        LL ans1=(1LL<<(L+1))-1-1;
        ans1=min(ans1,total-1);
        cout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<endl;
    }
}
