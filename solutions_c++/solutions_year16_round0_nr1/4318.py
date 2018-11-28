#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int tests;
ll n;
set<int> num_set;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("sabbir.txt","w",stdout);
    cin >> tests;
    for(int t=1;t<=tests;t++){
        cin >> n;
        if (n==0){
            printf("Case #%d: INSOMNIA\n",t);
        } else {
            //ll ans=0;
            ll m=2;
            ll tmp=n,last;
            while(1){
                last=tmp;
                while(tmp){
                    num_set.insert(tmp%10);
                    tmp/=10;
                }
                if(num_set.size()==10) break;
                tmp=n*(m++);
            }
            printf("Case #%d: %lld\n",t,last);
            num_set.clear();
        }


    }

}
