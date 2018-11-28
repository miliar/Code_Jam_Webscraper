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

int n,arr[2000],a[2000];

bool ctrl(){
    int ind=1;
    while( ind<n and a[ind]<a[ind+1] )  ind++;
    while( ind<n and a[ind]>a[ind+1] )  ind++;
    return ind==n;

}

map<int,int>    yer;

int F[134334];

void update( int x ){
    while(x){
        F[x]++;
        x -= x&-x;
    }
}

int query( int x ){
    int res=0;
    while(x<=40){
        res += F[x];
        x += x&-x;
    }
    return res;
}
int hesap(){
    memset( F,0,sizeof F );
    int res=0;
    FP( i,1,n ){
        res += query( yer[a[i]] );
        update( yer[a[i]] );
    }
    return res;

}

int main(){freopen("inp","r",stdin);
    freopen("out","w",stdout);
    int t;
    yer.clear();
    cin >> t;
    FP( q,1,t ){
    cin >> n;
    FP( i,1,n ){ cin >> arr[i]; yer[arr[i]]=i; a[i]=arr[i];}
    sort( a+1,a+n+1 );
    int mini=37462323;
    do{
        if( !ctrl() )   continue;
        mini = min( mini,hesap() );
    }while( next_permutation( a+1,a+n+1 ) );

    cout << "Case #" << q << ": " << mini << endl;
    }
}
