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

ll n,r,p,s;
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

string DP[3][20] = {""};

string CH[3] = {"P" , "R" , "S"};

string rek(ll id, ll level){

if(DP[id][level][0] != '-'){return DP[id][level];}
if(level == 0){
    return CH[id];
}
string ans = "";

string a1 = rek(id , level-1);
string a2 = rek((id+1)%3 , level-1);
ans = min(a1,a2) + max(a1,a2);

return ans;

}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	ll  z,a,b,c,x,y;
	ll c1,c2,c3,c4,c5;
    ll ans;
    ll k;
	string output = "";

	cin >> T;

    for(c1 = 0; c1 < 3; c1++){
            for(c2 = 0; c2 < 20; c2++){
                DP[c1][c2] = "-";
            }
        }

    for(c3 = 0; c3 < T; c3++){


        cin >> n >> r >> p >> s;

        string ans = "ZZZZZ";

        string s1 = rek(0 , n);

        ll r2 = 0;
        ll p2 = 0;
        ll s2 = 0;
        for(c1 = 0; c1 < s1.length(); c1++){
            if(s1[c1] == 'R'){r2++;}
            if(s1[c1] == 'P'){p2++;}
            if(s1[c1] == 'S'){s2++;}
        }
        if(r2 == r && s2 == s && p2 == p){
            ans = s1;
        }

        string S2 = rek(1 , n);

        r2 = 0;
        p2 = 0;
        s2 = 0;
        for(c1 = 0; c1 < S2.length(); c1++){
            if(S2[c1] == 'R'){r2++;}
            if(S2[c1] == 'P'){p2++;}
            if(S2[c1] == 'S'){s2++;}
        }
        //cout << S2 << ":  "<< r2 << " " << s2 << " " << p2 << "\n";
        if(r2 == r && s2 == s && p2 == p){
            ans = min(ans,S2);
        }

        string s3 = rek(2 , n);

        r2 = 0;
        p2 = 0;
        s2 = 0;
        for(c1 = 0; c1 < s3.length(); c1++){
            if(s3[c1] == 'R'){r2++;}
            if(s3[c1] == 'P'){p2++;}
            if(s3[c1] == 'S'){s2++;}
        }
        if(r2 == r && s2 == s && p2 == p){
            ans = min(ans,s3);
        }
        if(ans[0] == 'Z'){ans = "IMPOSSIBLE";}
        //cout << s1 << "  " << S2 << " " << s3 << "\n";
        cout << "Case #" << c3+1 << ": " << ans << "\n";
    }


	return 0;
}
