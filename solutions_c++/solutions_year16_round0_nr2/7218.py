#include <iostream>
#include <string>

using namespace std;

char flip(char c)
{
	if( c == '+' )
		return '-';
	else
		return '+';
}

bool swap( char* start, char* end )
{
	while( end >= start )
	{
		if( end == start )
			*start = flip(*start);
		else
		{
			char temp = *start;
			*start = flip(*end);
			*end = flip(temp);
		}

		start++;
		end--;
	}

	return true;
}

bool sort( char* start, char* end, char sort_order, unsigned int & out )
{
	if( end < start )
		return true;

	if( sort_order == *end )
		sort( start, end - 1, *end, out );
	else
	{
		sort( start, end - 1, *end, out );
		swap( start, end );
		out++;
	}
	return true;
}

bool Execute(char* input_start, char* input_end, unsigned int & out)
{
	sort( input_start, input_end, '+', out );
	return true;
}

int main_PC() 
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) 
	{
		string input = "";
		cin >> input;
		unsigned out = 0;
		
		Execute( (char*)input.c_str(), (char*)input.c_str() + (input.length() - 1), out );
		
		cout << "Case #" << i+1 << ": " << out << endl;
	}

	return 0;
}

int main()
{
	main_PC();
	
	return 0;
}