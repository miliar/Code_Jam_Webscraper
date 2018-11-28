// Syed Ghulam Akbar
// CodeJam 2014

#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		long N=0, war=0, deceitWar=0, start=0, end=0;
		double Naomi[1001], Ken[1001];

		// Get the blocks of both Noami and Ken
		cin  >> N;

		for (int i=0; i<N; i++)
			cin >> Naomi[i];

		for (int i=0; i<N; i++)
			cin >> Ken[i];

		// Now before doing any processing, sort both the arrays
		sort(Naomi, Naomi+N);
		sort(Ken, Ken+N);
	
		// Store the start and end counters for used blocks
		start = 0, end = N-1;

		// Calculate the game points if both play the fair war game
		for (int i=N-1; i>=0; i--)
		{
			// Naomi will win this point for sure
			if (Naomi[i] > Ken[end])
				war++;
			else 
				end--;
		}

		// Calculate the game points if Naomi plays deceitful war
		long index = 0, found=0;
		for (int i=0; i<N; i++)
		{
			// check if this number is greator than any of Ken numbers
			for (int j=index; j<N; j++)
				if (Naomi[i] > Ken[j])
				{
					deceitWar++;
					index++;
					found = 1;
					break;
				}
		}
	

		cout << "Case #" << test << ": " << deceitWar << " " << war << endl;

		//for (int i=0; i<N; i++)
		//	cout << Naomi[i] << " ";
		//cout << endl;
		//for (int i=0; i<N; i++)
		//	cout << Ken[i] << " ";
		//cout << endl;
	}
}
