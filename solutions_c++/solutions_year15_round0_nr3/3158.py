#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

template<typename T>
T read(){
	T temp;
	cin >> temp;
	return temp;
}

struct Quat{
	char letter;
	char sign;
	static const Quat table[][4];
	static const char translate[4];
	
	Quat( char l, bool sign=false ) : sign( sign ? 1 : 0 ){
		for( letter=0; letter<sizeof(translate); letter++ )
			if( translate[letter] == l )
				break;
	}
	
	string asString() const{
		string s;
		if( sign )
			s += '-';
		s += translate[letter];
		return s;
	}
	
	Quat& operator*=( const Quat& q2 ){
		auto& q = table[letter][q2.letter];
		letter = q.letter;
		sign = q.sign ^ sign ^ q2.sign;
		return *this;
	}
	
	bool operator==( const Quat& q2 ) const{ return letter == q2.letter && sign == q2.sign; }
};

const Quat Quat::table[4][4] = {
		{ { '1' }, { 'i'       }, { 'j'       }, { 'k'       } }
	,	{ { 'i' }, { '1', true }, { 'k'       }, { 'j', true } }
	,	{ { 'j' }, { 'k', true }, { '1', true }, { 'i'       } }
	,	{ { 'k' }, { 'j'       }, { 'i', true }, { '1', true } }
	};

const char Quat::translate[4] = { '1', 'i', 'j', 'k' };


struct Dijkstra{
	int x;
	vector<Quat> letters;
	
	Dijkstra(){
		auto l = read<int>();
		x = read<int>();
		for( int i=0; i<l; i++ )
			letters.emplace_back( read<char>() );
	}
	
	bool get( int offset, int iteration, int position=0 ) const{
		static const vector<Quat> ijk = { {'i'}, {'j'}, {'k'} };
		
		if( position >= ijk.size() )
			return iteration == x-1 && offset == letters.size(); //if we reached the end, we have a solution
		if( offset >= letters.size() ){
			offset = 0;
			iteration++;
		}
		if( iteration >= x )
			return false;
				
		auto q = letters[offset];
		if( q == ijk[position] )
			if( get( offset+1, iteration, position+1 ) )
				return true;
		
		for( offset++; iteration < x; offset=0, iteration++ ){
			for( int i=offset; i<letters.size(); i++ ){
				q *= letters[i];
				if( q == ijk[position] )
					if( get( i+1, iteration, position+1 ) )
						return true;
			}
		}
		return false;
	}
	
	bool result(){
		return get( 0, 0, 0 );
	};
};


int main(){
	auto amount = read<int>();
	
	for( int i=1; i<=amount; i++ )
		cout << "Case #" << i << ": " << (Dijkstra().result() ? "YES" : "NO") << endl;
	
	return 0;
}
