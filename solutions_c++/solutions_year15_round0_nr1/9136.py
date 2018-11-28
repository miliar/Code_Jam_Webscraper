#include <fstream>
#include <string>

using namespace std;

//#define SMALL_TEST

#ifdef SMALL_TEST
	char inFile[] = "A-small-attempt2.in";
	char outFile[] = "A-small-attempt2.out";
#else
	char inFile[] = "A-large.in";
	char outFile[] = "A-large.out";
#endif


int main(int argc, char** argv)
{
	ifstream in(inFile);
	ofstream out(outFile);

	if (!in.is_open())
		printf("Can't find input file: %s\n", inFile);

	if(!out.is_open())
		printf("Can't open %s to write.\n", outFile);

	int numTest;
	in >> numTest;

	int maxShyness;
	string shynessDist;

	for (int i = 0; i < numTest; ++i)
	{
		in >> maxShyness >> shynessDist;

		unsigned int extra = 0;
		unsigned int sum = 0;
		for (size_t j = 0; j < shynessDist.size(); ++j)
		{
			int currentDigit = stoi(shynessDist.substr(j,1));
			int sofar = sum + extra;

			if ((currentDigit != 0) && (sofar < j))
				extra += j - sofar;

			sum += currentDigit;
		}
		out << "Case #" << i+1 << ": " << extra << endl;
	}

	in.close();
	out.close();
	return 0;
}