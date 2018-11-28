#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);

using namespace std ;
ll  n,i,j,k,t,flag,y,r,lo,hi,m,ans,x,cnt,i1,j2,k1,x1,y2,q;
ll a[5000008],b[5000008],c[3000] ;
pair<ll,ll> p[500008] ;
//map<pair<ll,ll>,ll> > m1 ;

vector<ll> v[100002] ;



ll convert_to_base(ll x1,ll y2){
j2 = 0 ; k1=1;
while(x1){
        j2 += (x1%2)*k1 ;
    x1=x1/2 ; k1=k1*y2 ;
}
return j2 ;
}


ll prime(ll x1){
    ans = 0 ;
for(i1=2;i1<=sqrt(x1);i1++){
    if(x1%i1==0){ans = i1 ; break;}
}
return ans ;
}

void print(){
    x1 = i ; y2 = 0;
while(x1){
     b[y2++] = x1%2 ;
    x1=x1/2 ;
}

for(x1=15;x1>=0;x1--){cout << b[x1] ;}
cout << " " ;
for(x1=2;x1<=10;x1++){cout << a[x1]<< " " ;}
cout << endl ;
}

int main(){

 freopen("input.txt","r",stdin) ;
 freopen("output.txt","w",stdout) ;

string s ;
k =1 ;
for(i=0;i<=16;i++){c[i] = k ; k = k*2 ;}

cin >> t ;  m=1;

while(t--){
cin >> n >> q ;
cnt = 0 ;
cout << "Case #" << m << ":\n" ;

for( i = c[n-1]+1 ; i<c[n] ; i++){
        //cout << i << endl ;
        if(cnt==q){break;}
        flag=1;
    for(j=2;j<=10;j++){
        x = convert_to_base(i,j) ;
//cout << x << endl ;
        if(x%j==1){
        if(prime(x)!=0){a[j]= prime(x);}
        else{flag=0;break ;}
        }
    else{flag=0;break ;}
    }
   if(flag){print();cnt++;}

}
m++;
}
}

