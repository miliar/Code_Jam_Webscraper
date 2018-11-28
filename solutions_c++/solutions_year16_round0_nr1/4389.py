#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int  MOD=1000000007;
const int  INF= int(1e9);

int main()
{
	ios_base::sync_with_stdio(false);
    int testCases;
    cin>>testCases;
    for(int k=1;k<=testCases;k++) {
        map<ll,bool> seen;
        vi done(20);
        ll n,res;
        cin>>n;
        bool insomnia=false;
        for(int i=n; ;i+=n) {
            ll temp=i;
            if(seen[temp]) {
                cout<<"Case #"<<k<<": "<<"INSOMNIA"<<"\n";
                insomnia=true;
                break;
            }
            seen[temp]=true;
            while(temp > 0) {
                int d=temp%10;
                done[d]=1;
                temp/=10;
            }
            bool ok=true;
            for(int j=0;j<=9;j++) {
                if(!done[j]) {
                    ok=false;
                    break;
                }
            }
            if(ok) {
                res=i;
                break;
            }
        }
        if(!insomnia) {
            cout<<"Case #"<<k<<": "<<res<<"\n";
        }
    }
	return 0;

}
