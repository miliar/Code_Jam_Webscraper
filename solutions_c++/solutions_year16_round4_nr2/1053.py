#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <fstream>
#include <sstream>

using namespace std;
typedef long long ll;
typedef long double ld;
ll big = 1000000007ll;

ll n,r,p,s,k;
ll T;



string nts(ll x){
    ostringstream ss;
    ss << x;
    return ss.str();
}

ll ctn(char ch){
    if(ch == '0'){return 0;}
    if(ch == '1'){return 1;}
    if(ch == '2'){return 2;}
    if(ch == '3'){return 3;}
    if(ch == '4'){return 4;}
    if(ch == '5'){return 5;}
    if(ch == '6'){return 6;}
    if(ch == '7'){return 7;}
    if(ch == '8'){return 8;}
    if(ch == '9'){return 9;}
    return -1;
}

ll pow(ll a, ll p){
if(p == 0){return 1;}
ll b = pow(a,p/2);
if(p%2 == 0){return b*b;}
else{return b*b*a;}
}

ld DP[201][201][101] = {0.0};
vector<ld> P;
ld P2[201] = {0};


ld dp(ll yes, ll no, ll i){

if(yes < 0 || no < 0){return ld(0);}
if(yes == 0 && no == 0){return ld(1);}
if(i == k){return ld(0);}

if(DP[yes][no][i] > 0.0){return DP[yes][no][i];}

ld ans = P2[i] * dp(yes-1 , no , i+1) + (ld(1)-P2[i]) * dp(yes , no-1 , i+1);
DP[yes][no][i] = ans;

//cout << "yes: " << yes << "   no: " << no << "  i: " << i << "  -  " << ans << "\n";

return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	ll  z,a,b,c,x,y;
	ll c1,c2,c3,c4,c5;
    ll ans;

	string output = "";

	cin >> T;

    for(c3 = 0; c3 < T; c3++){
        cin >> n >> k;
        P.clear();
        for(c1 = 0; c1 < k/2+1; c1++){
            for(c2 = 0; c2 < k/2+1; c2++){
                for(c4 = 0; c4 < n+1; c4++){
                    DP[c1][c2][c4] = 0.0;
                }
            }
        }
        for(c1 = 0 ;c1 < n; c1++){
            ld pr;
            cin >> pr;
            P.push_back(pr);
        }
        sort(P.begin() , P.end());
        ll two = 1;
        for(c1 = 0; c1 < n; c1++){
            two *= 2;
        }

        ld ans = 0;

        for(c1 = 0; c1 < two; c1++){
            ll n1 = 0;
            vector<ll> bits;
            ll ct = c1;
            for(c2 = 0; c2 < n; c2++){
                n1 += (ct%2);
                bits.push_back(ct%2);
                if(ct%2 == 1){
                    P2[n1-1] = P[c2];
                }
                ct/=2;
            }

        if(n1 == k){


                for(c2 = 0; c2 < k/2 + 1; c2++){
                    for(c4 = 0; c4 < k/2+1; c4++){
                        for(c5 = 0; c5 < k+1; c5++){
                            DP[c2][c4][c5] = ld(0);
                        }
                    }
                }

            ld test = dp(k/2,k/2,0);
            if(test > ans){
                ans = test;
                /*
                for(c2 = 0; c2 < n; c2++){
                    cout << bits[c2] << " ";
                }cout << "\n";*/
            }

        }
        }


        cout << setprecision(18) << "Case #" << nts(c3+1) << ": " << ans << "\n";
    }



	return 0;
}
