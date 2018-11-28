#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <utility>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main()
{
	unsigned t;
	cin >> t;
	
	for( unsigned i = 1; i <= t; ++i )
	{
		unsigned firstRow;
		cin >> firstRow;

		vector<vector<unsigned>> firstTab( 4, vector<unsigned>( 4 ) );
		for( auto&& row : firstTab )
		{
			for( auto&& card : row )
			{
				cin >> card;
			}
		}
		vector<unsigned> firstCandidates = firstTab[firstRow-1];

		unsigned secondRow;
		cin >> secondRow;

		vector<vector<unsigned>> secondTab( 4, vector<unsigned>( 4 ) );
		for( auto&& row : secondTab )
		{
			for( auto&& card : row )
			{
				cin >> card;
			}
		}
		vector<unsigned> secondCandidates = secondTab[secondRow - 1];

		map<unsigned, unsigned> repetitions;
		for( auto&& card : firstCandidates )
		{
			++repetitions[card];
		}
		for( auto&& card : secondCandidates )
		{
			++repetitions[card];
		}

		unsigned coutOfTwos = 0;
		unsigned candidate;
		for( auto&& element : repetitions )
		{
			if( element.second == 2 )
			{
				candidate = element.first;
				++coutOfTwos;
			}
		}

		string answer;
		if( coutOfTwos == 0 )
		{
			answer = "Volunteer cheated!";
		}
		else if( coutOfTwos == 1 )
		{
			answer = to_string( candidate );
		}
		else
		{
			answer = "Bad magician!";
		}

		cout << "Case #" << i << ": " << answer << endl;
	}

	return 0;
}
