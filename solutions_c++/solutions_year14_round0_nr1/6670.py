#include<bits/stdc++.h>

using namespace std;

typedef long long L;

int main()
{
    /*
    #ifndef ONLINE_JUDGE
        freopen("int.txt","r",stdin);
    #endif // ONLINE_JUDGE
*/
    ios_base::sync_with_stdio(false);

    int T, a, b;
    int x[4][4], y[4][4];
    int cnt, ans;

    cin>>T;

    for(int t=1; t<=T; t++) {
        cnt=0;

        cin>>a;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                cin>>x[i][j];
            }
        }

        cin>>b;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                cin>>y[i][j];
            }
        }

        a--;b--;

        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                if(x[a][i]==y[b][j]) {
                    cnt++;
                    ans = x[a][i];
                }
            }
        }

        cout<<"Case #"<<t<<": ";

        if(cnt==1) {
            cout<<ans<<endl;
        } else if (cnt==0) {
            cout<<"Volunteer cheated!"<<endl;
        } else {
            cout<<"Bad magician!"<<endl;
        }
    }

    return 0;
}
