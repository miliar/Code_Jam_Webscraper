#include<bits/stdc++.h>
using namespace std;

int ar[10];

void dig( long long n)
{
	while( n )
	{
		ar[n % 10]++;
		n /= 10;
	}
}

int main()
{
	ofstream fout ("a.out");
    	ifstream fin ("a.in");
	long long tes;
	fin >> tes;
	long long n, inp;
	for( long long u = 0; u < tes; u++ )
	{	
		fout << "Case #" << u + 1 << ": ";
		fin >> inp;
		for( long long i = 0; i < 10; i++ )
		{
			ar[i] = 0;
		}
		n = inp;
		int fl;
		do
		{
			dig( n );
			fl = 1;
			for( long long i = 0; i < 10; i++ )
			{
				//cout << ar[i] << ' ';
				if( ar[i] == 0 )
				{
					fl = 0;
					break;
				}
			}
			n += inp;
		}
		while(inp != 0 && fl == 0 );
		n -= inp;
		if( n == 0 )
			fout << "INSOMNIA\n";
		else
			fout << n << '\n';
	}
	return 0;
}
		
		
		
