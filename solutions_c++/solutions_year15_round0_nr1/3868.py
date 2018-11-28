#include <iostream>
#include <fstream>
#include <cstdlib>



/*


4
4 11111
1 09
5 110011
0 1


*/
int main (int argc, char* argv[])
{

	std::ifstream in(argv[1]);
	std::ofstream out("out.txt");

	if (!in || !out)
	{
		std::cout << "Input/output error." << std::endl;
		return(-1);
	}


	int test_count;
	in >> test_count;

	for(int i = 0; i < test_count; ++i)
	{
		int max_shy;
		std::string ppl;
		int result = 0;
		in >> max_shy >> ppl;

		char buf[2];
		buf[1] = '\0';
		int standing = 0;
		for(int n = 0; n < ppl.size(); ++n)
		{
			while(n > standing)
			{
				++result;
				++standing;
			}
			buf[0] = ppl[n];
			standing += atoi(buf);
		}
		
		out << "Case #" << i + 1 << ": " << result << std::endl;
	}

	in.close();
	out.close();

	return 0;
}