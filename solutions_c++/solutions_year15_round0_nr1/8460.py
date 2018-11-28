#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
	int CASE_NUM = 0;

	// open input file
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("result.out");

	// load case number
	fin >> CASE_NUM;
	//cout << "Case number : " << CASE_NUM << endl;

	//CASE_NUM = 3;
	for (int ti = 0; ti < CASE_NUM; ti++)
	{
		int smax = 0;
		int fcount = 0; // number of necessary friends
		int standCount = 0; // number of standed audiences
		char* buf = 0;

		// load S max
		fin >> smax;

		buf = new char[smax + 2];
		fin >> buf;
		//cout << "[" << ti << "] " << buf << endl;

		for (int i = 0; i < smax + 1; i++)
		{
			int num = (int)(buf[i] - '0');
			if (num == 0)
			{
				continue;
			}
			else if (standCount < i)
			{
				int need = i - standCount;
				fcount += need;
				standCount += need;
			}

			standCount += num;
		}

		// result
		fout << "Case #" << ti + 1 << ": " << fcount << endl;
	}

	fin.close();
	fout.close();
}