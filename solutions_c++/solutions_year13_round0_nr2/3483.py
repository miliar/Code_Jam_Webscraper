//Use Visual Studio Express 2008 to compile
// cj13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
using namespace std;
map<unsigned long,vector<pair<unsigned long,unsigned long>>> sq;
unsigned long temp;
bool used[200];
unsigned long N,M,T;
bool process() {
	cin >> N >> M;
	sq.erase ( sq.begin(), sq.end() );
	for( unsigned long i = 0; i < N; i++ ) {
		for( unsigned long j = 0; j < M; j++ ) {
			cin >> temp;
			sq[temp].push_back( pair<unsigned long,unsigned long>(i,j) );
		}
	}
	for( unsigned short i = 0; i < N + M; i++ ) {
		used[i] = false;
	}
	for ( map<unsigned long,vector<pair<unsigned long,unsigned long>>>::reverse_iterator it = sq.rbegin(); it != sq.rend(); it++ ) {
		/*cout << it->first << "\n";
		for ( unsigned short i = 0; i < it->second.size(); i++ )
			cout << it->second[i].first << it->second[i].second << "\n";*/
		vector<pair<unsigned long,unsigned long>>* v = &it->second;
		for ( unsigned short i = 0; i < v->size() ; i++ ) {
			if ( used[(*v)[i].first] && used[(*v)[i].second+N] )
				return false;
		}
		for ( unsigned short i = 0; i < v->size() ; i++ ) {
			used[(*v)[i].first] = true;
			used[(*v)[i].second+N] = true;
		}
	}
	return true;
}
int _tmain(int argc, _TCHAR* argv[])
{
	cin >> T;
	for( unsigned long i = 0; i < T; i++ ) {
		if( process() )
			cout << "Case #" << i+1 << ": YES\n";
		else
			cout << "Case #" << i+1 << ": NO\n";
	}
	return 0;
}

