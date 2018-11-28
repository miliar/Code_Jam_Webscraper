#include <iostream>
#include <string>

using namespace std;

int index[26];
bool p = false;
char digits[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

char answer[10];
int kkk = 0;

bool set( char* dig )
{
	bool res = true;
	char* d = dig;
	while( *d )
	{
		index[(*d) - 'A'] = index[(*d) - 'A'] - 1;
		if( index[(*d) - 'A'] < 0 )
		{
			res = false;
		}
		d++;
	}
	return res;
}

bool unset( char* dig )
{
	char* d = dig;
	while( *d )
	{
		
		index[(*d) - 'A'] = index[(*d) - 'A'] + 1;
		d++;
	}
	return true;
}

bool CheckFor(int d, char* input)
{
	bool allzero = true;
	for(int i = 0; i < 26; i++)
	{
		if( index[i] > 0 )
		{
			allzero = false;
		}
	}
	if( allzero == true )
	{
		p = true;
		return true;
	}

	for( int i = d; i < 10; i++ )
	{
		if( set( digits[i] ) )
		{
			if( CheckFor( i, input ) )
			{
				if( p )
					answer[kkk++] = i;
				return true;
			}
			else
			{
				unset(digits[i]); 
			}
		}
		else
		{
			unset(digits[i]);
		}
	}
	return false;
}

int main() 
{
	int t;
	cin >> t;
	for (int k = 0; k < t; ++k) 
	{
		kkk = 0;
		for(int i = 0; i < 10; i++ )
		{
			answer[i] = -1;
		}

		string input = "";
		cin >> input;

		for( int i = 0; i < 26; i++ )
		{
			index[i] = 0;
		}

		char* c = (char*)input.c_str();
		while( *c )
		{
			index[(*c) - 'A']++;
			c++;
		}

		CheckFor( 0, (char*)input.c_str() );

		cout << "Case #" << k + 1 << ": ";

		for( int i = 9; i >= 0; i-- )
		{
			if( answer[i] != -1 )
			{
				cout << (int)answer[i];
			}
		}
		cout << endl;

	}

	return 0;
}