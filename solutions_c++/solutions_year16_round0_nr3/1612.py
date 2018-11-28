#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>
#include <bitset>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for(int i=0; i<numCases; i++)
	{
		int N, J;
		cin >> N >> J;

		cout << "Case #" << i+1 << ": " << endl;
		int start = 1 << N/2-1;
		start += 1;

		int shift = 1 << N/2;
		for(int i=start; i<J*2+start; i+=2)
		{
			int final = i*(shift) + i;
			if (N == 6)
			{
				bitset<6> bitFinal(final);
				cout << bitFinal;
			}
			if (N == 16)
			{
				bitset<16> bitFinal(final);
				cout << bitFinal;
			}
			else if (N == 32)
			{
				bitset<32> bitFinal(final);
				cout << bitFinal;
			}

			for(int j=0; j<9; j++)
				cout <<fixed << " " << (long long)pow(j+2,(N/2))+1;
			cout << endl;
		}
	}

	return 0;
}