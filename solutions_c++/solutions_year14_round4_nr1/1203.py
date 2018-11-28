#include<bits/stdc++.h>

#define FP( ii,aa,bb )  for(int ii=aa;ii<=bb;ii++)
#define FM( ii,aa,bb )  for(int ii=aa;ii>=bb;ii--)
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define st  first
#define nd  second
#define mp  make_pair
#define pb  push_back
#define all(gg) gg.begin(),gg.end()
#define lli long long int
using namespace std;

lli n,X;
lli arr[100000];
multiset<lli>    S;

int main(){
    freopen("inp","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin >> t;
    FP( q,1,t ){
    cin >> n >> X;
    FP( i,1,n ){ cin >> arr[i];
        S.insert( arr[i] );
    }
    int res=0,x;
    multiset<lli>::iterator it;
    while( S.size() ){
        res++;
        x = *S.begin();
        S.erase( S.begin() );
        if( !S.size() ) continue;
        it = S.upper_bound( X-x );
        if( S.begin()==it ) continue;
        it--;
        S.erase(it);
    }
    cout << "Case #" << q << ": " << res << endl;
    }
}
