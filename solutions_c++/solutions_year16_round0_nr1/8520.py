#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

int main() {

	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile;
	outfile.open("A-large_out.txt");

	int test;
	infile >> test;

	for (int t = 0; t < test; ++t)
	{

		int cnt = 1;
		int n;
		int k;
		int c;
		int temp;
		set<int>ss;

		infile >> n;


		if (n == 0) outfile << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
		else
		{
			while (1)
			{

				temp = n*cnt;
				while (1)
				{
					k = temp % 10;
					ss.insert(k);
					if (temp / 10 == 0) { ss.insert(temp); cnt++; break; }
					else temp = temp/10;

				}
				if (ss.size() == 10) break;

			}
			outfile << "Case #" << t + 1 << ": " << n*(cnt-1) << endl;
		}

	}

	infile.close();
	outfile.close();

	return 0;
}