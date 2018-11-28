#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);

using namespace std ;
ll  n,i,j,k,t,flag,y,r,lo,hi,m,x,cnt,q,z,l;
ll a[200][200],b[2666],c[5000],ans[100] ;
pair<ll,ll> p[500008] ;


vector<ll> v,u ;


int main(){

freopen("input.txt","r",stdin) ;
freopen("output.txt","w",stdout) ;
string s ;
cin >> t ;
m = 1 ;
while(t--){

cin >> n ;
for(i=1;i<=2500;i++){b[i] = 0 ;c[i] = 0 ;}

for(i=0;i<(2*n-1);i++){
    for(j=0;j<n;j++){
        cin >> a[i][j] ; b[a[i][j]]++;
    }
}
for(i=1;i<=2500;i++){
    if(b[i]%2!=0){
        v.pb(i) ;
    }
}

sort(v.begin(),v.end()) ;
cout << "Case #" << m << ": " ;
for(i=0;i<v.size();i++){
    cout << v[i] << " " ;
}
cout << endl ;
v.clear() ; m++ ;}


}
