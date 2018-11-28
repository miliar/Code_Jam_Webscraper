#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>

using namespace std;


int main() 
{ 
	int size = 0;
	std::ios_base::sync_with_stdio(false);

	std::ifstream in("A-large.in");
	 cin.tie(NULL);

	int caseSize;
	in >> caseSize;

	std::ofstream out("A-large.out", ios::out | ios::binary);

	for(int i = 0; i < caseSize; ++i)
	{
		int numberOfPieces = 0;
		in >> numberOfPieces;

		std::vector<int> pieces;
		int speed = 0;
		for (int i = 0; i < numberOfPieces; ++i)
		{
			int piece = 0;
			in >> piece;
			pieces.push_back(piece);
			if (i != 0)
			{
				if(pieces[i - 1] > pieces[i])
					speed = std::max(speed, pieces[i - 1] - pieces[i] );
			}
		}

		int variant1 = 0;
		int variant2 = 0;

		for (int i = 0; i < numberOfPieces - 1; ++i)
		{
			if(pieces[i + 1] < pieces[i])
				variant1 += pieces[i] - pieces[i + 1] ;
			
			variant2 += std::min(pieces[i], speed);
		}

		out << "Case #" << i+1 <<": " << variant1 << " " << variant2 << "\n";
	}



	out.close();

	return 0; 
}