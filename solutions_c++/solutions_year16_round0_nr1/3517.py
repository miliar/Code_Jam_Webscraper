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
cin >> n ;
for(i=0;i<=9;i++){a[i]=0 ;}
if(n==0){cout <<"Case #" << m << ": INSOMNIA\n" ;}
else{
cnt = 0 ; x = n ;  f(x) ;
while(cnt!=10){
    x += n ;
    f(x) ;
}
cout <<"Case #" << m << ": " <<  x << endl ;
}
m++;
}

}
