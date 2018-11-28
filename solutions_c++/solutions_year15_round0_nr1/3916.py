#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <string>
#include <queue>
#include <functional>
#include <stack>
#include <complex>
#include <stdlib.h>
#include <string.h>
using namespace std;

namespace{
	#define		CAST( T, val )		( (T)( val ) )
	#define		CASE( lb )			break; case lb:
	#define		CASE_CONTINUE( lb )	case lb:
	#define		CASE_DEFAULT		break; default:
	#define		For( i, s )			for(int i= 0; i< (int)s; i++)
	#define		ForA( i, a, s )		for(int i= (int)a; i< (int)s; i++)
	#define		ForSize( i, s )		for(int i= 0, size= (int)s; i< size; i++)
	#define		ForSizeA( i, a, s )	for(int i= (int)a, size= (int)s; i< size; i++)
	#define		ForItr( itr, con )	for(auto itr= con.begin(); itr!= con.end(); itr++)
	#define		ForStr( i, str )	for(int i= 0; str[i]; i++)
	#define		GOTO( lb )			goto lb
	#define		LABEL( lb )			lb:

	typedef		long long		LLint;
	typedef		unsigned int	Uint;
	typedef		unsigned char	Uchar;
	typedef		unsigned short	Ushort;
	
	const int Ten5= 100000;		//	10^5
	const int Ten6= 1000000;	//	10^6
	const double EPS= 0.00000000023283064365386962890625;	//	2^-32
	template <typename T> class priority_queue_less : public priority_queue<T,vector<T>,greater<T> >{};
}

void solve(){
	int n;
	cin>> n;
	n++;

	char str[1024];
	int ppl[1024];
	cin>> str;
	For( i, n ){
		ppl[i]= str[i] -'0';
	}

	int sum= ppl[0];
	int max= 0;
	ForA( s, 1, n ){
		if( ppl[s] ){
			max= ::max( max, s -sum );
			sum+= ppl[s];
		}
	}

	cout<< max;
}
int main(){
	int L;
	cin>> L;

	For( l, L ){
		cout<< "Case #"<< l+1<< ": ";
		solve();
		cout<< endl;
	}

	return 0;
}
