#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

	ifstream infile;
	infile.open("B-large.in");
	ofstream outfile;
	outfile.open("B-large_out.txt");

	int test;
	infile>> test;

	for (int t = 0; t < test; ++t)
	{

		int cnt = 0;
		string n;
		infile >> n;
		int k;

		for (int i = 1; i < n.length(); ++i)
		{
			if (n[i - 1] != n[i])
				cnt++;
		}
		if (n[n.length() - 1] == '-') cnt++;

		outfile << "Case #" << t + 1 << ": " << cnt << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}