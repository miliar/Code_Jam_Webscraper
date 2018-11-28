#include <cstdio>
#include <time.h>
#include <cstdlib>
#include <random>
#include <iostream>
using namespace std;

int find(int N, bool* found, int numFound)
{
	int finN = 0;
	while ( numFound != 10 )
	{
		finN += N;
		int finN2 = finN;
		while ( finN2 >= 1 ){ 
			int t = finN2 % 10;
			if (!found[t]){ found[t] = true; numFound++; }
			finN2 /= 10;
		}
	}
	return finN;
}

int main(void)
{
	int T;
	cin >> T;
	
	for ( int c = 0; c < T; c++ )
	{
		int N; cin >> N;
		cout << "Case #" << (c+1) << ": ";
		if ( N == 0 ){ cout << "INSOMNIA" << endl; }
		else { 
			bool found[10]; for (int c = 0; c < 10; c++ ){ found[c] = false; } 
			cout << find(N, found, 0) << endl;
		}
	}
	
	return 0;
}