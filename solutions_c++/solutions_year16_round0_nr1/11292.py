#include <bits/stdc++.h>
using namespace std;
int v[15];
int main() {
//    freopen("in.in","r",stdin);
//    freopen("out.out","w",stdout);
    int t,n,cas=1;
    cin>>t;
    while(t--){
        cin>>n;
        printf("Case #%d: ",cas++);
        if(!n){
            puts("INSOMNIA");
            continue;
        }
        memset(v,0,sizeof v);
        int i=1,cnt=0;
        while(1){
            int m=n*i;
            while(m){
                if(!v[m%10]){
                    cnt++;
                    v[m%10]=1;
                }
                m/=10;
            }
            if(cnt==10)
                break;
            i++;
        }
        cout<<n*i<<endl;
    }
	return 0;
}
