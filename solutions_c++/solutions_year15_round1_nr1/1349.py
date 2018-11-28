#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>

int main(int argc, char* argv[])
{
	std::ifstream infile;
	std::ofstream outfile;
	std::string outfilename;
	outfilename.assign(argv[1]);
	outfilename.append(".out");
	infile.open(argv[1]);
	outfile.open(outfilename);

	int T;
	infile>>T;
	for(int Case=1; Case<=T; ++Case)
	{
		int N;
		infile>>N;

		int totalDrop=0;
		int maxDrop=0;
		std::vector<int> nVals;
		nVals.resize(N);
		infile >> nVals[0];
		for(int i = 1; i < N; ++i)
		{
			infile>>nVals[i];

			if(nVals[i-1]-nVals[i] > 0)
				totalDrop+=(nVals[i-1]-nVals[i]);
	
			if((nVals[i-1]-nVals[i]) > maxDrop)
				maxDrop = (nVals[i-1]-nVals[i]);
		}

		int secondSum=0;
		for(int i=0; i<N-1; ++i)
		{
			if(nVals[i] >= maxDrop)
				secondSum+=maxDrop;
			else
				secondSum+=nVals[i];
		}

		outfile<<"Case #"<<Case<<": ";
		outfile<<totalDrop<<" "<<secondSum;
		outfile<<std::endl;
	}
	infile.close();
	outfile.close();
	return 0;
}