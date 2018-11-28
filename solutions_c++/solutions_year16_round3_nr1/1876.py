#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);

using namespace std ;
ll  n,i,j,k,flag,y,r,lo,hi,m,x,cnt,q,z,t,ans,sum,i1, ans1,ans2;
ll a[5000000],b[5000000],c[5000000];


map<string,ll> m1,m2 ;
vector<pair<string,string> > v ;
string s   ;
pair<ll,char> p[200] ;


int main(){


freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
cin >> t ;
z=1;

while(t--){
char d = 'A' ;
for(i=0;i<26;i++){p[i].ss = d ; d++ ;}
 cout << "Case #" << z << ": "; z++;

cin >> n ; sum=0;
for(i=0;i<n;i++){cin >> p[i].ff ; sum += p[i].ff;}
sort(p,p+n) ;

if(sum%2!=0){cout << p[n-1].ss << " " ; p[n-1].ff--;}

 sort(p,p+n) ;

while(p[n-1].ff>0){
 sort(p,p+n) ;
 if(p[n-1].ff-p[n-2].ff>=2){
    cout << p[n-1].ss <<p[n-1].ss << " ";        p[n-1].ff--;p[n-1].ff--;
 }
 else{
     cout << p[n-1].ss << p[n-2].ss << " ";     p[n-1].ff--; p[n-2].ff--;
 }
  sort(p,p+n) ;
}

cout << endl ;

}

}
