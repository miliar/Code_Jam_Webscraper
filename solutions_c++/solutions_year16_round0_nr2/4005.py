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

int t;
char s[200];

int main(){
	int t,id=0;
	cin >> t;
	while( t-- ){
		cin >> s+1;
		int n = strlen( s+1 );
		int	res=0;
		char p = '+';
		FM( i,n,1 ){
			if( s[i]==p )	continue;
			if( s[1]==p ){
				res++;
				p = '+' + '-' - p;
				continue;
			}
			res++;
			FP( j,1,i ) s[j] = '+' + '-' - s[j];
			reverse( s+1,s+i+1 );
		}
		cout << "Case #" << (++id) << ": " << res << endl;
	}
}
