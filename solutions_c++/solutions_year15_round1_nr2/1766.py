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

inline LLint Gcd(LLint a, LLint b){ LLint c; while(c= a%b){ a= b; b= c; } return b; }
void solve(){
	int B, N;
	struct{
		int time;
		int wait;
	} M[1000];

	priority_queue_less<int> canCut;

	cin>> B>> N;
	For( i, B ){
		cin>> M[i].time;
		M[i].wait= 0;
	}

	LLint lcm= 1;
	For( i, B ) lcm= lcm*M[i].time /Gcd( lcm, M[i].time );
	
	LLint mod= 0;
	For( i, B ){
		mod+= lcm/M[i].time;
	}
	if( N> mod ){
		N-= CAST( int ,( N/mod -1 ) *mod );
	}

	int min;
	while(1){
		min= INT_MAX;
		For( i, B ){
			min= ::min( min, M[i].wait );
		}
		For( i, B ){
			M[i].wait-= min;
			if( M[i].wait== 0 ) canCut.push( i );
		}

		while( canCut.empty()== false ){
			if( --N ){
				M[ canCut.top() ].wait= M[ canCut.top() ].time;
				canCut.pop();
			}else{
				cout<< canCut.top() +1;
				return ;
			}
		}
	}
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
