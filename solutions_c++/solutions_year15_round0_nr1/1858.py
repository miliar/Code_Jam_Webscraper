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

        int t;
        cin>>t;
        int j = 0;
        while(j<t){
            int x;
            cin>>x;
            string s;
            cin>>s;
            int p = 0;
            int stoji = 0;
            for(int i=0; i<s.length(); i++){
                while(stoji<i && s[i]!='0'){
                    p++;
                    stoji++;

                }
                stoji+=s[i]-'0';
            }
            cout<<"Case #"<<j+1<<": "<<p<<en;
            j++;
        }

}
