#include <algorithm>
#include <string>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cassert>
#include <queue>
#include <cstdlib>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lli long long int
#define all( gg )	gg.begin(),gg.end()
#define foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define FP( ii,aa,bb ) for( int ii=aa;ii<=bb;ii++ )
#define FM( ii,aa,bb ) for( int ii=aa;ii>=bb;ii-- )

using namespace std;

int m,n,maxi,s;
string str[100];

void rec( int ind,set<string>	*p ){
	if( ind==m+1 ){
		FP( i,1,n )	if( !p[i].size() )	return;
		int ymax=0;
		FP( i,1,n )	ymax += p[i].size();
		if( ymax>maxi ){
			maxi = ymax;
			s = 1;
		}
		else if( ymax==maxi )	s++;
		return;
	}
	set<string>	arr[6];
	arr[1] = p[1];
	arr[2] = p[2];
	arr[3] = p[3];
	arr[4] = p[4];
	FP( i,1,n ){
		FP( j,0,str[ind].size() )
			arr[i].insert( str[ind].substr( 0,j ) );
		rec( ind+1,arr );
		arr[i] = p[i];
	}
}

int main(){

	freopen("inp","r",stdin);
	freopen("out","w",stdout);

	int t;
	cin >> t;
	FP( q,1,t ){
		maxi = 0;
		s = 0;
		cin >> m >> n;
		FP( i,1,m )
			cin >> str[i];
		set<string>	arr[6];
		rec( 1,arr );
		cout << "Case #" << q << ": " << maxi << " " <<s << endl;
	}	
	
}
