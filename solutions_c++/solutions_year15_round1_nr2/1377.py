#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <numeric>

int gcd(int a, int b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b)
{
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}


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
		int B,N;
		infile>>B;
		infile>>N;
		int *M = new int[B];
		for(int i=0; i<B; ++i)
			infile>>M[i];

		int LCM = std::accumulate(M, M + B, 1, lcm);
		int cycleSize = 0;
		for(int i=0; i<B; ++i)
			cycleSize+=LCM/M[i];
		N=(N-1)%cycleSize + 1;

		std::vector<int> Barbers;
		Barbers.resize(B);
		for(int i=0; i<B; ++i)
			Barbers[i]=0;

		int solution=-1;
		int min = 0;
		while(N>0)
		{
			int newMin=1000000;
			for(int i=0; i<B; ++i)
			{
				Barbers[i]-=min;
				if(Barbers[i]==0)
				{
					--N;
					Barbers[i] = M[i];
					if(N==0)
					{
						solution = i+1;
						break;
					}
				}
				if(Barbers[i] < newMin)
					newMin = Barbers[i];
			}
			min=newMin;
		}

		outfile<<"Case #"<<Case<<": ";
		outfile<<solution;
		outfile<<std::endl;

		delete[] M;
	}
	infile.close();
	outfile.close();
	return 0;
}