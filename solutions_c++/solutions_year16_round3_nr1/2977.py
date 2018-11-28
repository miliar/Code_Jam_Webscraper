#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <bitset>
#include <assert.h>
#include <string>
#include <map>
#include <functional>

using namespace std;

const int NotFound = -1;

char letter( int index )
{
	return 'A' + index;
}

void add( int index, string& result )
{
	if( !result.empty() ) {
		result += " ";
	}
	result += letter( index );
}

void add( int index1, int index2, string& result )
{
	if( !result.empty() ) {
		result += " ";
	}
	result += letter( index1 );
	result += letter( index2 );
}



int main()
{
	ifstream input("f:\\Input.txt", std::ifstream::in);
	//istream& input = cin;
	ofstream output("f:\\Output.txt", std::ofstream::out);

	int t;
	input >> t;

	for( int i = 0; i < t; i++ ) {
		int n;
		input >> n;
		multimap<int, int, std::greater<int>> data;
		for( int j = 0; j < n; j++ ) {
			int jCount;
			input >> jCount;
			data.insert( pair<int, int>( jCount, j ) );
		}

		string result = "";
		while( !data.empty() ) {
			multimap<int, int>::iterator biggest1 = data.begin();
			multimap<int, int>::iterator biggest2 = biggest1;
			biggest2++;
			multimap<int, int>::iterator biggest3 = biggest2;
			biggest3++;

			if( data.size() == 3 && biggest1->first == 1 && biggest2->first == 1 && biggest3->first == 1 ) {
				add( biggest1->second, result );
				add( biggest2->second, biggest3->second, result );
				break;
			} else if ( biggest1->first == biggest2->first ) {
				pair<int, int> b1 = *biggest1;
				pair<int, int> b2 = *biggest2;
				add( b1.second, b2.second, result );
				data.erase( biggest1 );
				data.erase( biggest2 );
				if( b1.first > 1 ) {
					b1.first--;
					b2.first--;
					data.insert( b1 );
					data.insert( b2 );
				} else {
					break;
				}
			} else {
				pair<int, int> b1 = *biggest1;
				pair<int, int> b2 = *biggest2;
				int delta = b1.first - b2.first;
				for( int j = 0; j < delta; j++ ) {
					add( b1.second, result );
				}
				data.erase( biggest1 );
				b1.first -= delta;
				data.insert( b1 );
			}
		}

		output << "Case #" << (i + 1) << ": " << result << endl;
	}
	
	return 0;
}