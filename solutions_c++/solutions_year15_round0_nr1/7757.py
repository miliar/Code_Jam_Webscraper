#include <iostream>
#include <string>
#include <map>
#include <fstream>


using namespace std;

int main()
{
	int T, S_max, count;
	string s;	
	cin >> T;
	map<char, int> m1;
	m1['0'] = 0;
	m1['1'] = 1;
	m1['2'] = 2;
	m1['3'] = 3;
	m1['4'] = 4;
	m1['5'] = 5;
	m1['6'] = 6;
	m1['7'] = 7;
	m1['8'] = 8;
	m1['9'] = 9;
	
	for( int i = 0; i < T; i++ )
	{
		cin >> S_max >> s;
		count = 0;
		int new_count = 0;	
		if( s != "" )
		{
			for( int j = 0; j < S_max + 1; j++ )
			{
				if( count < j )
				{
					new_count++;
					count++;				
				}				
				count += m1[s[j]];
			}
			cout << "Case #" << ( i + 1 ) << ": " << new_count << endl;	
		}
		else
			cout << "Case #" << ( i + 1 )<< ": " << count << endl;
	}

	return 0;
}
