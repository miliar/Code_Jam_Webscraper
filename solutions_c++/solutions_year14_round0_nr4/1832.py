#include <iostream>
#include <fstream>
#include <iomanip> 
#include <string>

#include <algorithm>    // std::sort
#include <vector>       // std::vector
using namespace std;
void main()
{
	//ifstream in ("input.in");
	//ofstream out("output.out");
	ifstream in ("inputLarge.in");
	ofstream out("outputLarge.out");

	int T = 0;
	in >> T;

	for (int Case = 1; Case<=T; Case++)
	{
		int N = 0;
		in >> N;
		
		vector<float> w1;
		vector<float> w2;
		
		for (int i = 0; i < N*2; i++)
		{
			float temp = 0;
			in >> temp;
			if (i < N)
				w1.push_back(temp);
			else
				w2.push_back(temp);
		}
		
		sort(w1.begin(), w1.begin() + N);
		sort(w2.begin(), w2.begin() + N);

		//game 1
		int point1 = 0;
		int high = N-1;
		int low = 0;
		while ( high >= low )
		{
			if (w1.at(high) < w2.at(high-low))
			{
				low++;
			}
			else
			{
				point1 ++;
				high--;
			}
		}

		//game2
		int point2 = 0;
		for (int i = 0; i < N ; i++)
		{
			float t = w1.at(i);

			if ( w2.at(w2.size()-1) < t)
			{
				point2 += N-i;
				break;
			}

			for (int j = 0; j < w2.size(); j++)
			{
				if( t < w2.at(j) )
				{
					w2.erase(w2.begin() + j);
					break;
				}
			}
		}

		out<< "Case #" << Case <<": "<< point1 << " "<< point2 << endl;
	}

	in.close();
	out.close();
}