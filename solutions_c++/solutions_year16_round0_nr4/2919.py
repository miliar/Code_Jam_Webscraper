#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);

using namespace std ;
ll  n,i,j,k,t,flag,y,r,lo,hi,m,c,ans,x,cnt;
ll a[5000008],b[5000008] ;
pair<ll,ll> p[500008] ;
//map<pair<ll,ll>,ll> > m1 ;

vector<ll> v[100002] ;

void f(ll y){

while(y){
    if(a[y%10]==0){cnt++ ;a[y%10]=1; }
    y/=10 ;
}

}


int main(){

freopen("input.txt","r",stdin) ;
freopen("output.txt","w",stdout) ;

string s ;

cin >> t ;  m=1;
while(t--){
cin >> k >> c >> s  ;
cout << "Case #" << m << ": " ;
for(i=1;i<=k;i++){
    cout << i << " ";
}
cout << endl;
m++;
}

}
