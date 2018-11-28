#include <bits/stdc++.h>

typedef long long lld;

using namespace std;

char verify[][5] = {
				   {'Z', 'E', 'R', 'O', '.'}, 
				   {'W', 'T', 'O', '.', '.'}, 
				   {'U', 'F', 'O', 'R', '.'}, 
				   {'X', 'S', 'I', '.', '.'}, 
				   {'G', 'E', 'I', 'H', 'T'}, 
				   {'O', 'N', 'E', '.', '.'}, 
				   {'H', 'T', 'R', 'E', 'E'}, 
				   {'F', 'I', 'V', 'E', '.'}, 
				   {'S', 'E', 'V', 'E', 'N'}, 
				   {'I', 'N', 'N', 'E', '.'} 
				   };

int number[] = {  0,   2,   4,   6,  8,   1,   3,   5,   7,   9  };

int main(){
	
	freopen( "in", "r", stdin );
	freopen( "out", "w", stdout );

	int t;
	cin >> t;
	for( int tc = 1; tc <= t; ++tc ){
		map<char, int> letters;
		
		string text;
		cin >> text;
		vector< int > answer;
		
		for( int i = 0; i < (int)text.size(); ++i ){
			++letters[text[i]];
		}
		
		
		for( int i = 0; i < 10; ++i ){
			while( letters.count( verify[i][0] ) ){
				for( int j = 0; j < 5; ++j ){
					--letters[verify[i][j]];
					if(letters[verify[i][j]] == 0 ){
						letters.erase( verify[i][j] );
					}
				}
				answer.push_back( number[i] );
			}
			
		}
		
		sort(answer.begin(), answer.end());
		
		cout << "Case #" << tc << ": ";
		for( int i = 0; i < (int) answer.size(); ++i ){
			cout << answer[i];
		}
		cout << "\n";
	}
	return 0;
}
