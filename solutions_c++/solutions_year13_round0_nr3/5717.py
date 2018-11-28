#include<fstream>

using namespace std;

ifstream infile("in.in");
ofstream outfile("out.out");

int main()
{
	int numT;
	infile >> numT;
	int a,b,i = 1,count = 0;
	//Precompute fair n square :) .. 
	int fair_n_square[] = {1,4,9,121,484};

	while(true)
	{
		count = 0;
		infile >> a;
		infile >> b;
		
		if(infile.eof())
			break;
	
		outfile << "Case #" << i++ << ": ";

		for(int i = 0; i < 5; i++)
			if( fair_n_square[i] >= a && fair_n_square[i] <=b )
				count++;

		outfile << count << endl;
	}

	return 0;
}