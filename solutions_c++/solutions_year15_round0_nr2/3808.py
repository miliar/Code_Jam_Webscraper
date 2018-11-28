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
	#define		ALL( con )			con.begin(), con.end()

	typedef		long long		LLint;
	typedef		unsigned int	Uint;
	typedef		unsigned char	Uchar;
	typedef		unsigned short	Ushort;
	
	const int Ten5= 100000;		//	10^5
	const int Ten6= 1000000;	//	10^6
	const double EPS= 0.00000000023283064365386962890625;	//	2^-32
	template <typename T> class priority_queue_less : public priority_queue<T,vector<T>,greater<T> >{};
}

const int NUM= 1001;
int Mins[NUM][NUM];

int getMax(vector<int>& ar){
	int max= 0;
	ForItr( itr, ar ){
		max= ::max( max, *itr );
	}
	return max;
}
vector<int> divCake(vector<int>& p, int& cnt){
	vector<int> ret;
	int max= getMax( p );

	ForItr( itr, p ){
		if( *itr== max ){
			ret.push_back( *itr /2 );
			ret.push_back( *itr -*itr /2 );
			cnt++;
		}else{
			ret.push_back( *itr );
		}
	}

	return ret;
}
void init(){
	int* mins[NUM];
	For( i, NUM ){
		mins[i]= Mins[i];
		For( k, NUM ) mins[i][k]= 0xffff;
	}

	ForA( i, 1, NUM ){
		ForA( k, 1, i ){
			ForA( d, 1, i+1 ){
				mins[i][k]= ::min( mins[i][k], mins[i/d][k]+ mins[i-i/d][k] +1 );
			}
		}
		ForA( k, i, NUM ) mins[i][k]= 0;
		cerr<< i<< endl;
	}
}
void solve(){
	int D;
	cin>> D;
	
	vector<int> P(D);
	For( d, D ){
		cin>> P[d];
	}

	int* mins[NUM];
	For( i, NUM ) mins[i]= Mins[i];

	/*
	int min= getMax( P );
	int cnt= 0;
	while(1){
		P= divCake( P, cnt );

		if( min < cnt ) break;
		min= ::min( min, getMax( P ) +cnt );
	}

	cout<< min;
	*/

	int min= INT_MAX;
	int sum;
	int max= *max_element( ALL( P ) );
	ForA( i, 1, max+1 ){
		sum= 0;

		For( d, D ){
			sum+= mins[ P[d] ][i];
		}
		min= ::min( sum +i, min );
	}

	cout<< min;
}
int main(){
	int L;
	cin>> L;

	init();
	For( l, L ){
		cout<< "Case #"<< l+1<< ": ";
		solve();
		cout<< endl;
	}

	return 0;
}
