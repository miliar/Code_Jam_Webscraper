/*
 * This is my code,
 * my code is amazing...
 */
//Template v2.0
//iostream is too mainstream
#include<iostream>
#include<string>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<iomanip>
//clibraries
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
//defines
#define ll long long
#define lld long double
#define pll pair<ll,ll>
#define pld pair<lld,lld>
#define vll vector<ll>
#define vvll vector<vll>
#define INF 1000000000000000047
const char en='\n';
#define debug(x){cerr<<x<<en;}
#define prime 47
#define lprime 1000000000000000009
#define lldmin LDBL_MIN
#define MP make_pair
#define PB push_back
using namespace std;




int main(){
	ios::sync_with_stdio(false);

        int T;
        cin>>T;
        cout<<setprecision(15)<<fixed;
        for(int t=1; t<=T; t++){
            
            int n;
            cin>>n;
            lld V,tt;
            cin>>V>>tt;
            cout<<"Case #"<<t<<": ";
            if(n==1){
                lld r,c;
                cin>>r>>c;
            if(abs(tt-c)<0.000001)
                cout<<V/r<<en;
            else cout<<"IMPOSSIBLE"<<en;
            }
            else{
                lld r1,c1,r2,c2;
                cin>>r1>>c1>>r2>>c2;
                if(abs(c1-c2)<0.0000001){
                    lld suc=r1+r2;
                    if(abs(c2-tt)<0.000001)
                    cout<<V/suc<<en;
                    else cout<<"IMPOSSIBLE"<<en;
                    continue;
                }
                if((c1>tt && c2>tt) || (c1<tt && c2<tt)){
                    cout<<"IMPOSSIBLE"<<en;
                    continue;
                }
                lld v1=(tt*V-V*c1)/(c2-c1);
                lld v2=V-v1;
                lld res=(v1*c2+v2*c1)/V;
                //cout<<tt<<" "<<res<<en;
                //cout<<v1<<" "<<v2<<en;
                    cout<<max(v2/r1,v1/r2)<<en;



            }



        }


}
