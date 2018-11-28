#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <climits>
#include <ctime>
#include <sstream>

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

#define	mod	1000000007LL

using namespace std;

lli	n=16,j=50;

lli find(lli x,lli b){
	if( !x )	return 0;
	return	find(x/10,b)*b+x%10;
}

lli ctrl(lli x,lli b){
	x = find( x,b );
	if( x==2 )	return -1;
	if( x%2==0 )	return 2;
	for( int i=3;i*i<=x;i+=2 )
		if( x%i==0 )	return i;
	return -1;
}

int main(){
	int t;
	cin >> t;
	cout << "Case #1:" << endl;
	FP( i,0,(1<<(n-2))-1 ){
		if( !j )	break;
		lli p = 1 , t = i;
		FP( j,1,n-2 ){
			p = p*10 + (t&1);
			t /= 2;
		}
		p = p*10+1;

		int ok=1;
		FP( j,2,10 ){
			if( ctrl(p,j)==-1 ){
				ok = 0;
				break;
			}
		}
		if( ok==0 )	continue;
		j--;
		cout << p << " ";
		FP( j,2,10 ){
			cout << ctrl( p,j ) << " ";
		}
		cout << endl;
	}
}
