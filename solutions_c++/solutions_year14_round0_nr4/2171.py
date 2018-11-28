#include <iostream>
#include <cstdio>
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
#include <cassert>

using namespace std;

unsigned war( vector<double> naomis, vector<double> kens )
{
	assert( naomis.size() == kens.size() );
	sort( naomis.begin(), naomis.end() );
	sort( kens.begin(), kens.end() );

	unsigned score = 0;
	while( naomis.empty() == false )
	{
		assert( naomis.size() == kens.size() );

		float naomi = *naomis.begin();
		naomis.erase( naomis.begin() );

		auto it = std::upper_bound( kens.begin(), kens.end(), naomi );
		if( it == kens.end() )
		{
			++score;
			kens.erase( kens.begin() );
		}
		else
		{
			kens.erase( it );
		}
	}

	assert( naomis.empty() );
	assert( kens.empty() );
	return score;
}

unsigned deceifulWar( vector<double> naomis, vector<double> kens )
{
	assert( naomis.size() == kens.size() );
	sort( naomis.begin(), naomis.end() );
	sort( kens.begin(), kens.end() );

	unsigned score = 0;
	while( kens.empty() == false )
	{
		assert( naomis.size() == kens.size() );

		float ken = *kens.begin();
		kens.erase( kens.begin() );

		auto it = std::upper_bound( naomis.begin(), naomis.end(), ken );
		if( it == naomis.end() )
		{
			naomis.erase( naomis.begin() );
		}
		else
		{
			++score;
			naomis.erase( it );
		}
	}

	assert( naomis.empty() );
	assert( kens.empty() );
	return score;
}

int main()
{
	unsigned t;
	cin >> t;
	
	for( unsigned i = 1; i <= t; ++i )
	{
		unsigned n;
		cin >> n;

		vector<double> naomis( n );
		for( auto&& weight : naomis ) cin >> weight;
		vector<double> kens( n );
		for( auto&& weight : kens ) cin >> weight;

		unsigned warScore = war( naomis, kens );
		unsigned deceifulWarScroe = deceifulWar( naomis, kens );

		cout << "Case #" << i << ": " << deceifulWarScroe << " " << warScore << endl;
	}

	return 0;
}
