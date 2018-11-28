#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);

using namespace std ;
ll  n,i,j,k,t,flag,y,r,lo,hi,m,ans,x,cnt,q,z,l;
ll a[5000008],c[5000008] ;
pair<ll,ll> p[500008] ;


vector<char> v,u ;


int main(){

freopen("input.txt","r",stdin) ;
freopen("output.txt","w",stdout) ;
string s ;
cin >> t ;
m = 1 ;
while(t--){

 cin >> s ;
 v.pb(s[0]) ; j = 1 ; k = 0 ;
n = s.size() ;
 for(i=1;i<n;i++){

        if(k==0){
            if(s[i]>=v[0]){u.pb(s[i]) ; k++ ;}
            else{v.pb(s[i]) ; j++;}
        }
        else{
            if(s[i]>=u[k-1]){u.pb(s[i]) ; k++ ;}
            else{v.pb(s[i]) ; j++;}
        }
 }

 reverse(u.begin(),u.end()) ;
cout << "Case #" << m << ": " ;
 for(i=0;i<k;i++){cout << u[i];}
  for(i=0;i<j;i++){cout << v[i];}

v.clear() ; u.clear() ;
cout << endl ; m++ ;
}


}
