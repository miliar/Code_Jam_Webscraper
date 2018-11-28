#include <vector>
#include <iostream>
#define SIZE 4
#define LEFT 1
#define RIGHT 2
using namespace std;

void fill_B (char a  [SIZE][SIZE]  )
{
	char c;
	for ( int i = 0; i < SIZE; ++i ) {
		for ( int j = 0; j < SIZE; ++j ) {
			cin >> c;
			a[i][j] = c;
		}
	}
}

void print ( char a [SIZE][SIZE] ) 
{
	for ( int i = 0; i < SIZE; ++i ){
		for ( int j = 0; j < SIZE; ++j ) {
			cout << a[i][j];
		}
		cout << endl;
	}
}

char check_Row ( int pos, char a[SIZE][SIZE]  ) 
{
	char c;
	c = a[pos][0];
	for ( int i = 1; i < SIZE; ++i ) {
		if ( c == 'T' )
			c = a[pos][i];
		if ( a[pos][i] == '.' ){
			c = '.';
			break;
		}
		else if ( a[pos][i] != c && a[pos][i] != 'T' ) {
			c = 'N';
		}
	}
	return c;
}

char check_Column ( int pos, char a[SIZE][SIZE]  ) 
{
	char c;
	c = a[0][pos];
	for ( int i = 1; i < SIZE; ++i ) {
		if ( c == 'T' ) 
			c = a[i][pos];
		if ( a[i][pos] == '.' ){
			c = '.';
			break;
		}
		if ( a[i][pos] != c && a[i][pos] != 'T' ) {
			c = 'N';
		}
	}
	return c;
} 

char check_Diag ( char a[SIZE][SIZE], int o  ) 
{
	char c;
	if ( o == LEFT ) {
		c = a[0][0];

		for ( int i = 1; i < SIZE; ++i ) {
			if ( c == 'T' ) 
				c = a[i][i];
			if ( a[i][i] == '.' ){
				c = '.';
				break;
			}
			else if ( a[i][i] != c && a[i][i] != 'T' ) {
				c = 'N';
			}
			
		}
		return c;
	}

       else if ( o == RIGHT ) {
		c = a[3][0];

		for ( int i = 2; i >= 0; --i ) {
			if ( c == 'T' )
				c = a[i][3-i];
			if ( a[i][3-i] == '.' ) {
				c = '.';
				break;
			}

			else if ( a[i][3-i] != c && a[i][3-i] != 'T' ) {
				c = 'N';
			}
		}
		return c;
	}
	return 'N';
} 
		
char who_Won ( char a [SIZE][SIZE] )
{
	char c;
	int found_Ans = 0;
	char ans ;
	int found_Per = 0;
	vector <char> results;
	
	results.push_back(check_Diag ( a, LEFT ));	
	results.push_back(check_Diag ( a, RIGHT ));
	results.push_back(check_Row ( 0, a ));
	results.push_back(check_Column ( 0 , a ));
	results.push_back(check_Row ( 3, a ));
	results.push_back(check_Column ( 3 , a ));

	for ( int i = 1; i < SIZE; i++ ) {
		results.push_back(check_Row (i, a));
		results.push_back(check_Column (i,a));
	}

	for ( int i = 0; i < results.size(); ++i ) {
		if ( results[i] == '.' )
			found_Per = 1;
		
		else if ( results[i] != 'N' ){
			found_Ans = 1;
			ans = results[i];
		}
	}

	if ( found_Ans == 0 && found_Per == 1 ) 
		return 'U';
	else if ( found_Ans == 1 )
		return ans;
	else
		return 'N';
}
			
int main ()
{
	char a [SIZE][SIZE];
	int amount = 0;
	vector <char> results;
	cin >> amount;

	for ( amount; amount > 0; --amount ) {
		fill_B (a);
		results.push_back(who_Won(a));
	}

	for ( int i = 0; i < results.size() ; ++i ){ 
		if ( results[i] == 'N' )
			cout << "Case #" << i + 1 << ": " <<"Draw" << endl;
		else if ( results[i] == 'U' )
			cout << "Case #" << i + 1 << ": " << "Game has not completed" << endl;
		else
			cout << "Case #" << i + 1 << ": " << results[i] << " won" << endl;
	}
	return 0;
}
