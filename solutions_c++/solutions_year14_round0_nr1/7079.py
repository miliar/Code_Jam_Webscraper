#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("inp1.in","r",stdin);
    int t;
    cin>>t;
    cout.precision(7);
    cout << fixed;

    int a = 1;
    while(a <= t) {
        vector<int> m(20 , 0);
        int v1;
        cin>>v1;
        v1--;
        for(int i=0 ; i<4 ; i++ ) {
            for(int j=0 ; j<4 ; j++) {
                int x;
                cin>>x;
                if(i==v1) m[x] = 1;
            }
        }
        int v2;
        cin>>v2;
        v2--;
        int ans;
        int cnt = 0;
        for(int i=0 ; i<4 ; i++ ) {
            for(int j=0 ; j<4 ; j++) {
                int x;
                cin>>x;
                if(i==v2 && m[x] == 1 ) {

                    ans = x;
                    cnt++;
                }
            }
        }

        if(cnt == 1) cout<<"Case #"<<a<<": "<<ans<<endl;
        else if(cnt == 0) cout<<"Case #"<<a<<": "<<"Volunteer cheated!"<<endl;
        else if (cnt > 1) cout<<"Case #"<<a<<": "<<"Bad magician!"<<endl;
        a++;

    }
}
