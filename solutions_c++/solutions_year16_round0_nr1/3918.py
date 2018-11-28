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

lli	t,n;

int main(){
	int id=0;
	cin >> t;
	while( t-- ){
		cin >> n;
		lli p = n;
		lli last = 1;
		while( p ){
			last *= 10;
			p /= 10;
		}
		int mask=0;
		FP( i,1,1000 ){
			lli t = i*n;
			while( t ){
				mask |= (1<<(t%10));
				t /= 10;
			}
			if( mask == 1023 ){
				cout << "Case #" << (++id) << ": " << i*n << endl;
				break;
			}
		}
		if( mask!=1023 )
			cout << "Case #" << (++id) << ": INSOMNIA" << endl;
	}
}
