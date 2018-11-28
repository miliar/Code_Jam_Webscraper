#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	
	input.open("D-small-attempt0.in");
	output.open("output.txt");
	
	int T, K, C, S;
	input >> T;
	
	for(int t = 1; t <= T; t++)
	{
		output << "Case #" << t << ": ";
		input >> K >> C >> S;
		if((C == 1) && (S < K))
		{
			output << "IMPOSSIBLE" << endl;
		}
		else if(C == 1)
		{
			for(int i = 1; i <= K; i++)
			{
				output << i << " ";
			}
			output << endl;
		}
		else if(S < K/2)
		{
			output << "IMPOSSIBLE" << endl;
		}
		else
		{
			int place;
			for(int i = 0; i < ((K/2) + (K%2)); i++)
			{
				place = 2*K*i + 2*(i+1);
				if(place > (K*K))
				{
					place = K*K;
				}
				output << place << " ";
			}
			output << endl;
		}
	}
	
	input.close();
	output.close();
	
	return 0;
}
