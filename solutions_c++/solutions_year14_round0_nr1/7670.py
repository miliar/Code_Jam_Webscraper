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
int n;
cin>>n;
int m=n;
while(n--){
vector<set<int>> U,V;
U.resize(5);
V.resize(5);

int r1;
cin>>r1;
for(int i=1; i<=4; i++)
    for(int j=1; j<=4; j++){
    
        int t;
        cin>>t;
        U[i].insert(t);
    }



int r2;
cin>>r2;
for(int i=1; i<=4; i++)
    for(int j=1; j<=4; j++){
        int t; 
        cin>>t;
        V[i].insert(t);        
    }

int p=0;
int h;

for(auto it=U[r1].begin(); it!=U[r1].end(); it++)
    if(V[r2].find(*it)!=V[r2].end()){p++;h=*it;}
cout<<"Case #"<<m-n<<": ";
if(p==0)cout<<"Volunteer cheated!"<<endl;
else if(p>1){cout<<"Bad magician!"<<endl;}
else cout<<h<<endl;


    }














}


