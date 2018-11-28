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

    int T;
    double c,f,x;
    double ans, rate;

    cin>>T;

    for(int t=1; t<=T; t++) {
        cin>>c>>f>>x;
        ans=0;
        rate=2.0;

        while(true)
        {
            ans += c/rate;

            if(((x-c)/rate)<(x/(f+rate))) {
                ans += (x-c)/rate;
                break;
            } else {
                rate = rate + f;
            }
        }

        cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<ans<<endl;
    }

    return 0;
}
