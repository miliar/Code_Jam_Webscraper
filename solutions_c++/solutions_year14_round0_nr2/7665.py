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
#include<iomanip>
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

lld run(){
vector<lld>F;
F.resize(1000000);
lld c,f,x;
cin>>c>>f>>x;

F[0]=0;
for(int i=1; i<=100047; i++){
F[i]=F[i-1]+c/(2+f*(i-1));
}

lld mi=x/2;
for(int i=1; i<=100047; i++){
lld p=F[i]+x/(2+i*f);
mi=min(mi,p);
}

return mi;
}




int main(){
	ios::sync_with_stdio(false);

int t,u;
cin>>t;
u=t;
while(t--){
cout<<"Case #"<<u-t<<": "<<setprecision(15)<<fixed<<run()<<endl;

}




}


