/*
 * main.cpp
 *
 *  Created on: 30 ???, 2015 ?.
 *      Author: Tigran
 */



#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <sstream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

typedef std::vector< std::string > line_type;

void solve_easy_helper( int N, const std::vector< line_type >& lines,
		std::set< std::string >& en, std::set< std::string >& fr,
		int process_id,
		int& answer )
{
	std::vector< std::string > temp;
	std::set_intersection( en.begin(), en.end(), fr.begin(), fr.end(), std::back_inserter( temp ) );
	int curr_answer = (int)temp.size();
	if ( curr_answer >= answer )
		return;
	if ( process_id == N ) {
		answer = std::min( answer, curr_answer );
	}
	else {
		const int line_length = lines[ process_id ].size();
		std::vector< bool > effects( line_length );
		// Try english
		for ( int i = 0; i < line_length; ++i ) {
			const std::string& word = lines[ process_id ][ i ];
			effects[ i ] = (en.count( word ) == 0);
			if ( effects[ i ] )
				en.insert( word );
		}
		solve_easy_helper( N, lines, en, fr, process_id + 1, answer );
		for ( int i = 0; i < line_length; ++i ) {
			const std::string& word = lines[ process_id ][ i ];
			if ( effects[ i ] )
				en.erase( word );
		}
		// Try french
		for ( int i = 0; i < line_length; ++i ) {
			const std::string& word = lines[ process_id ][ i ];
			effects[ i ] = (fr.count( word ) == 0);
			if ( effects[ i ] )
				fr.insert( word );
		}
		solve_easy_helper( N, lines, en, fr, process_id + 1, answer );
		for ( int i = 0; i < line_length; ++i ) {
			const std::string& word = lines[ process_id ][ i ];
			if ( effects[ i ] )
				fr.erase( word );
		}
	}
}

int solve_easy( int N, std::vector< line_type >& lines )
{
	std::set< std::string > en, fr;
	std::copy( lines[ 0 ].begin(), lines[ 0 ].end(), std::inserter( en, en.begin() ) );
	std::copy( lines[ 1 ].begin(), lines[ 1 ].end(), std::inserter( fr, fr.begin() ) );
	int answer = (N + 5) * (1000 + 5);
	std::random_shuffle( lines.begin() + 2, lines.end() );
	solve_easy_helper( N, lines, en, fr, 2, answer );
	return answer;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int N;
		cin >> N;
		std::string temp;
		std::getline( cin, temp );
		std::vector< line_type > lines;
		for ( int i = 0; i < N; ++i ) {
			line_type l;
			std::getline( cin, temp );
			std::istringstream istr( temp );
			while ( istr >> temp ) {
				l.push_back( temp );
			}
			lines.push_back( l );
		}
		cout << "Case #" << tc << ": ";
		cout << solve_easy( N, lines ) << endl;
	}

	return 0;
}

