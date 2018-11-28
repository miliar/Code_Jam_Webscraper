#include<bits/stdc++.h>

using namespace std;

typedef long long L;

int main()
{

    #ifndef ONLINE_JUDGE
        freopen("int.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // ONLINE_JUDGE

    ios_base::sync_with_stdio(false);

    int T;
    cin>>T;

    for(int t=1; t<=T; t++) {
        int a,b,k;

        cin>>a>>b>>k;
        int cnt=0;

        for(int i=0; i<a; i++) {
            for(int j=0; j<b; j++) {
                if((i&j) < k) {
                    cnt++;
                }
            }
        }

        cout<<"Case #"<<t<<": "<<cnt<<endl;
    }

    return 0;
}
