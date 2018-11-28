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
        for(int tt=1; tt<=t; tt++){
            int d;
            cin>>d;
            vll V;
            for(int i=0; i<d; i++){
                int x;
                cin>>x;
                V.PB(x);
            }

            int naj = 1000000;
            for(int i=1; i<=1000; i++){
                int pocet = 0;
                for(int j=0; j<V.size(); j++){
                    
                        pocet+=(V[j]-1)/i;
                    
                    

                }
                naj = min(naj,pocet+i);
            }



            cout<<"Case #"<<tt<<": "<<naj<<en;

        }


}
