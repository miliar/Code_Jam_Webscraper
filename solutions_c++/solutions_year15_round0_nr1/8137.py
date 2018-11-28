#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream ifs("D:\\TestProjects\\Programs\\Debug\\SOInput.txt");
	ofstream ofs("D:\\TestProjects\\Programs\\Debug\\SOOuput.txt");

	int tc; ifs >> tc;
	int t = 0;
	while (t < tc) {
		int Smax; ifs >> Smax;
		string strshy; ifs >> strshy;

		int f = 0;

		int i = 0, n = 0;
		int j = strshy[i] - '0';
		n += j;
		i++;

		while (i < (Smax+1))
		{
			j = strshy[i] - '0';

			if (n >= i)
			{
				n += j;
			}
			else
			{
				f += (i-n);
				n += (i-n);
				n += j;
			}

			i++;
		}

		ofs << "Case #" << t+1 << ": " << f << endl;
		t++;
	}

}