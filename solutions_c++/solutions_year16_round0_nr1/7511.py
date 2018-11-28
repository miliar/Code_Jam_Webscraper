#include<bits/stdc++.h>
using namespace std;
#define int long long
main() {
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cnt,n,test;
    bool check[10];
    cin >> test,n;
    for(int i=1;i<=test;i++){
        memset(check,0,10);cnt=0;
        int zz = 0;
        cin >> n;
        while(1){
            cnt++;
            int tmp = n*cnt;
            while(tmp>0) {zz= zz + 1 - check[tmp%10]; check[tmp%10]=1;tmp/=10;}
            if (zz == 10 || cnt >10000) break;
        }
        if (zz == 10) cout << "Case #" << i << ": " << n*cnt << endl;
        else cout << "Case #" << i << ": INSOMNIA" <<  endl;
    }
}
