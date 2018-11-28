// lm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;
pair<int,int> ExtremumsInRow( vector<vector<int>> & table, int row ) {
	int minval = 100, maxval = 0;
	for( int c = 0; c < table[0].size(); c++ ) {
		minval = min( table[row][c], minval );
		maxval = max( table[row][c], maxval );
	}
	return pair<int,int>( minval, maxval );
}
bool CutRow( vector<vector<int>> &table, vector<vector<int>> &current, int r, int h ) {
	unsigned R = table.size();
	unsigned C = table[0].size();
	bool cancut = true;
	for( unsigned c = 0; c < C; c++ ) {
		if( table[r][c] > h ) { cancut = false; break; }
	}
	if( cancut ) for( unsigned c = 0; c < C; c++ ) current[r][c] = h;
	return cancut;
}
bool CutCol( vector<vector<int>> &table, vector<vector<int>> &current, int c, int h ) {
	unsigned R = table.size();
	unsigned C = table[0].size();
	bool cancut = true;
	for( unsigned r = 0; r < R; r++ ) {
		if( table[r][c] > h ) { cancut = false; break; }
	}
	if( cancut ) for( unsigned r = 0; r < R; r++ ) current[r][c] = h;
	return cancut;
}
bool TablesEqual( vector<vector<int>> & a, vector<vector<int>> & b ) {
	unsigned R = a.size();
	unsigned C = a[0].size();
	for( unsigned r = 0; r < R; r++ )
		for( unsigned c = 0; c < C; c++ )
			if( a[r][c] != b[r][c] ) return false;
	return true;
}
string CanMakePattern( vector<vector<int> > & table, set<int>& hts ) {
	set<int>::reverse_iterator rit = hts.rbegin();
	vector<int> row( table[0].size(), 100 );
	vector<vector<int>> current( table.size(), row );
	unsigned R = table.size();
	unsigned C = table[0].size();
	while( rit != hts.rend() ) {
		if( TablesEqual( table, current ) ) return "YES";
		int h = *rit;
		int numCuts = 0;
		for( unsigned r = 0; r < R; r++ ) numCuts += CutRow( table, current, r, h );
		for( unsigned c = 0; c < C; c++ ) numCuts += CutCol( table, current, c, h );
		if( numCuts == 0 ) break;
		++rit;
	}
	return TablesEqual( table, current ) ? "YES" : "NO";
}
int _tmain(int argc, _TCHAR* argv[])
{
	string mainfile = "large.txt";
	string infile = string("../") + mainfile;
	string outfile = string("../out") + mainfile;
	cout << outfile << endl;
	ifstream data( infile );
	ofstream outdata( outfile );
	int T = 0;
	data >> T;
	for( int t = 1; t <= T; t++ ) {
		int N, M;
		data >> N >> M;
		vector<int> _row( M, 0 );
		vector< vector<int> > table( N, _row );
		set<int> hts;
		for( int i = 0; i < N; i++ )
			for( int j = 0; j < M; j++ ) {
				data >> table[i][j];
				hts.insert( table[i][j] );
			}
		string result = CanMakePattern( table, hts );
		cout << "Case #" << t << ": " << result << endl;
		outdata << "Case #" << t << ": " << result << endl;
	}
	outdata.close();
	cin >> T;
	return 0;
}

