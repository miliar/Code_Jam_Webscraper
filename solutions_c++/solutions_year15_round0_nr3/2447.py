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

class Input{
public:
	//	L [ 1, 10000 ], X [ 1, 10^12 ]
	LLint X;
	int L, idx;
	char str[10001];

	char getChar(){
		if( idx== L ){
			X--;
			if( X ){
				idx= 0;
				return str[idx++];
			}else{
				return NULL;
			}
		}else{
			return str[idx++];
		}
	}
	void init(){
		cin>> L>> X;
		cin>> str;
		idx= 0;
	}
};

void init(){
}
void solve(){
	Input input;
	input.init();

	enum{
		ST_I, ST_J, ST_K, ST_END,
	} state= ST_I;
	char map[256][256];
	bool sym[256][256]= { false };

	map['1']['1']= '1';
	map['1']['i']= 'i';
	map['1']['j']= 'j';
	map['1']['k']= 'k';
	map['i']['1']= 'i';
	map['i']['i']= '1';	sym['i']['i']= true;
	map['i']['j']= 'k';
	map['i']['k']= 'j';	sym['i']['k']= true;
	map['j']['1']= 'j';
	map['j']['i']= 'k';	sym['j']['i']= true;
	map['j']['j']= '1';	sym['j']['j']= true;
	map['j']['k']= 'i';
	map['k']['1']= 'k';
	map['k']['i']= 'j';
	map['k']['j']= 'i';	sym['k']['j']= true;
	map['k']['k']= '1';	sym['k']['k']= true;
	
	char now= '1', next;
	bool s= false;
	while( char in= input.getChar() ){
		s^= sym[now][in];
		next= map[now][in];

		switch( state ){
			CASE( ST_I ){
				if( next== 'i' ){
					state= ST_J;
					now= '1';
				}else{
					now= next;
				}
			}
			CASE( ST_J ){
				if( next== 'j' ){
					state= ST_K;
					now= '1';
				}else{
					now= next;
				}
			}
			CASE( ST_K ){
				if( next== 'k' ){
					state= ST_END;
					now= '1';
				}else{
					now= next;
				}
			}
			CASE( ST_END ){
				now= next;
			}
		}

		/*
		if( s ) cout<< "-";
		cout<< now<< " -> ";
		//*/
	}

	if( state== ST_END && now== '1' && s== false ){
		cout<< "YES";
	}else{
		cout<< "NO";
	}
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
