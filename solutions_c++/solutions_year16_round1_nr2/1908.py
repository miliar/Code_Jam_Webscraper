#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define rep(i,a,b) for(int i=a;i<b;i++)

using namespace std;

int map_val[2600];


int main() {
    freopen("f2.in","r",stdin);
    freopen("f2.out","w",stdout);

    int T;
    cin>>T;
    rep(t,1,T+1) {
        int n;
        cin>>n;
        int ans[n];
        memset(map_val,0,sizeof map_val);
        int tmp;
        rep(i,0,2*n-1) {
            rep(j,0,n) {
                    cin>>tmp;
                    map_val[tmp]++;
            }

        }
        int cnt=0;
        rep(i,0,2600) {
            if(map_val[i]%2) {
                ans[cnt++]=i;

            }
            if(cnt==n)
                break;
        }
        sort(ans,ans+n);
        cout<<"Case #"<<t<<": ";
        rep(i,0,n) {
            cout<<ans[i]<<' ';
        }
        cout<<endl;




    }
}
