#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<set>

using namespace std;
vector<string> word ( { "XSI", "WTO", "ZERO", "GEIHT", "HTREE", "SEVEN", "RFOU", "VFIE", "INNE", "ONE" } );
int num[10] = {6, 2, 0, 8, 3, 7, 4, 5, 9, 1};

void solve( int casenum )
{
	multiset<char> ms;
	cout << "Case #" << casenum << ": ";
	string s;
	cin >> s;
	for ( int i = 0 ; i < s.size() ; i++ )
		ms.insert(s[i]);
	multiset<int> digmap;
	for ( int i = 0 ; i < 10; i++ )
	{
		for ( auto iter = ms.find( word[i][0] ); 
				iter != ms.end(); 
				iter = ms.find( word[i][0] ) )
		{
			for ( int j = 0 ; j < word[i].size() ; j++ )
			{
				auto iter2 = ms.find( word[i][j] );
				ms.erase(iter2);
			}
			digmap.insert( num[i] );
		}
	}
	for ( auto iter = digmap.begin(); iter != digmap.end() ; iter++ )
		cout << *iter;
	cout << endl;
};
int main(int argc, char * argv[] )
{
	int t;
	cin >> t;
	for ( int casenum = 1; casenum <= t; casenum++ )
	{
		solve( casenum );
	}

}
