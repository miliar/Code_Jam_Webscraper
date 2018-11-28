#include <iostream>
#include <vector>
#include <fstream>

using namespace std ;

int main()
{
	ifstream in;
	in.open("Magic.in");

	ofstream out;
	out.open("Magic.out");

	int N,R;
	int C [4][4];
	bool first [16];
	vector<int> poss;
	in >> N;
	for(int count = 1; count <= N ; count ++)
	{
		poss = vector<int>(0);
		for(int i = 0 ; i < 16 ; i ++)
			first[i] = false;

		in >> R;
		for(int i = 0 ; i < 4 ; i ++)
			for(int j = 0 ; j < 4 ; j ++)
				in >> C[i][j];
		for(int i = 0 ; i < 4 ; i ++)
			first[C[R - 1][i] - 1] = true;

		in >> R;
		for(int i = 0 ; i < 4 ; i ++)
			for(int j = 0 ; j < 4 ; j ++)
				in >> C[i][j];

		for(int i = 0 ; i < 4 ; i ++)
			if(first[C[R - 1][i] - 1])
				poss.push_back(C[R - 1][i]);

		out << "Case #" << count << ": ";
		if(poss.size() == 0)
			out << "Volunteer cheated!";
		else if(poss.size() > 1)
			out << "Bad magician!";
		else
			out << poss[0];

		out << endl;

	}
	return 0 ;
}