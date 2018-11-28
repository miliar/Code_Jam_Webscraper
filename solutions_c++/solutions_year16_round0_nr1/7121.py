#pragma once
#include <iostream>

using namespace std;

void SetBitmap( unsigned int n, unsigned int & bitmap )
{
	while( n > 0 )
	{
		int i = n % 10;
		n = n / 10;
		int temp = 1;
		temp = temp << i;
		bitmap = bitmap | temp; 
	}
}

bool Execute(unsigned int n, unsigned int & out)
{
	if( 0 == n )
		return false;

	unsigned int bitmap = 0;
	unsigned int iloop = 0;

	while( bitmap != 1023 )
	{
		SetBitmap( n * (++iloop), bitmap );
	}

	out = n * (iloop);
	return true;
}

void main_CS() 
{
	unsigned int t, n;
	cin >> t;
	for (unsigned int i = 0; i < t; ++i) 
	{
		cin >> n;
		unsigned int out;
		
		if( Execute( n, out) )
			cout << "Case #" << i+1 << ": " << out << endl;
		else
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
	}
}

int main()
{
	main_CS();


	return 0;
}