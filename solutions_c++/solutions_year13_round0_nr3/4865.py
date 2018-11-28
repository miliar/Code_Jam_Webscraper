#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("out.txt");
	int T, A, B, X;
	int count[1005];

	cin >> T;

	memset( count, 0, sizeof count );
	
	for( int i = 1 ; i <= 1000; ++i )
	{
		count[i] = count[i-1]; 
		if( i == 1 || i == 4 || i == 9 || i == 121 || i == 484 )
			count[i]++;
	}

	for( int i = 0 ; i < T; ++i )
	{
		cin >> A >> B;
		cout << "Case #" << i + 1 << ": " << count[B] - count[A-1];
		if( i != T - 1 ) cout << endl;
	}
}