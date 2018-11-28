#include <bits/stdc++.h>

#define	st first
#define	nd second
#define	mp make_pair
#define	pb push_back
#define	lli long long int
#define	all( gg )	gg.begin(),gg.end()
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	FP( ii,aa,bb ) for( lli ii=aa;ii<=bb;ii++ )
#define	FM( ii,aa,bb ) for( lli ii=aa;ii>=bb;ii-- )
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;

#define	eps	1e-5
#define	sifir( aa )	( abs(aa)<eps )
#define	esit( aa,bb )	( sifir( (aa)-(bb) ) )

using namespace std;

int	n;
vector<int>	a[30];

lli	Exp=211,mod=1000007;

lli	gethash( string s ){
	lli	H=0;
	foreach( s,it )
		H = (H*Exp+(*it))%mod;
	return	H;
}

int	h[2000000],vis,h2[2000000];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int	t,id=0;
	cin >> t;
	while( t-- ){
		cerr << t << endl;
		cin >> n;
		string	s,p;
		getline( cin,s );
		FP( i,1,n )	a[i].clear();
		FP( i,1,n ){
			getline( cin,s );
			istringstream in(s);
			while( in>>p ){
				a[i].pb( gethash(p) );
			}
		}

		int	res = mod;
		FP( mask,0,(1<<n)-1 ){
			if( (mask&1) or !(mask&2) )	continue;
			int	s = 0;
			vis++;
			FP( i,1,n )
				if( (mask&(1<<i-1)) )
					foreach( a[i],it )
						h[*it] = vis;
				else
					foreach( a[i],it )
						h2[*it] = vis;
			FP( i,1,n )
				if( (mask&(1<<i-1)) )
					foreach( a[i],it )
						if( h[*it]==vis and h2[*it]==vis ){
							s++;
							h[*it] = 0;
						}
			res = min( res,s );
		}
		printf("Case #%d: %d\n",++id,res);
	}
}

