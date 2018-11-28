#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int palindrome( int num )
{
	string tmp;
	string rev;
	while( num )
	{
		tmp += num%10;
		num /= 10;
	}
	for( int i = tmp.size()-1 ; i >= 0 ; i-- )
	{
		rev += tmp[i];
	}
	if( rev == tmp )
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int main()
{
	FILE* fIn;
	FILE* fOut;
	fIn = fopen( "C-small-attempt0.in", "r" );
	fOut = fopen("Output.out", "w" );
	int Test_case;
	fscanf( fIn, "%d", &Test_case );
	vector<int> save;
	for( int i = 1 ; i <= 1000 ; i++ )
	{
		if( palindrome(i) == 1 )
		{
			save.push_back(i);
		}
	}
	for( int TC = 1 ; TC <= Test_case ; TC++ )
	{
		int count = 0;
		int start, end;
		fscanf( fIn, "%d %d", &start, &end );
		for( int i = 0 ; i < save.size() ; i++ )
		{
			int temp = save[i]*save[i];
			if( temp < start || temp > end )
			{
				continue;
			}
			string tmp;
			string rev;
			while( temp )
			{
				tmp += temp%10;
				temp /= 10;
			}
			for( int i = tmp.size()-1 ; i >= 0 ; i-- )
			{
				rev += tmp[i];
			}
			if( tmp == rev )
			{
				count++;
			}
		}
		fprintf( fOut, "Case #%d: %d\n", TC, count);
	}
	return 0;
}