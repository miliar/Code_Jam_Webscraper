#include<bits/stdc++.h>
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define eb emplace_back
#define pb push_back
#define ll long long
#define mp make_pair
#define x first
#define y second
#define mod 1000000007
#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b
using namespace std;
void solve(int n,int q)
{
    for(int i=0;i<(1<<n);++i){
            if((i&(1<<0))==0){
                continue;
            }
            if((i &(1<<(n-1)))==0){
                continue;
            }
            int flag=0;
            ll res=0;
            string s="";
            vector<ll> sd;
             for(int k=0;k<n;++k){
                    if(i & (1<<k))

                        s+="1";
                        
                    else
                        s+="0";

                }
                reverse(s.begin(),s.end());
            for(int j=2;j<=10;++j){
                ll f=1;res=0;
                for(int k=0;k<n;++k){
                    if(i & (1<<k)){
                        res+=f;

                        }


                    f=f*j;
                }
                /*if(j==4)
                    cout << res << "\n";*/
                for(ll k=2;k<=sqrt(res);++k){
                    if(res%k==0){
                       sd.pb(k);
                       break;
                    }
                }
            }
            if(sd.size()==9){
                --q;
                cout << s << " ";
                for(int i=0;i<9;++i)
                    cout << sd[i] << " ";
                cout << "\n";
            }
            if(q==0){
                break;
            }
        }
}
int main(){
    int t;
    cin >> t;
    int jx;
    rep(jx,0,t){
        int n,q;
        cin >> n >> q;
        cout << "Case #" << jx+1 << ": " << "\n";
        solve(n,q);
    }   
    return 0;
}
