#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <time.h>

using namespace std;

int main()	
{
	int N, P, Q;
	string str;
	ifstream ifs("A-small-attempt0.in");
	ofstream ofs("A-small-attempt0.out");
	streambuf *cin_backup;

	cin_backup = cin.rdbuf();
	cin.rdbuf(ifs.rdbuf());

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> str;
		int index = str.find_first_of('/');
		int powNum = 0;
		P = stoi(str.substr(0, index));
		Q = stoi(str.substr(index+1, str.length()-index-1));

		int R = Q;
		while (R != 0)
		{
			R = R&(R-1);
			powNum++;
		}

		if (powNum != 1)
			ofs << "Case #" << i+1 << ": " << "impossible" << endl;
		else
		{
	        R = P;
			int powNum1 = 0;
			while ((R = R>>1) != 0)
				powNum1++;

			R = Q;
			int powNum2 = 0;
			while ((R = R>>1) != 0)
			powNum2++;

			ofs << "Case #" << i+1 << ": " << powNum2-powNum1 << endl;
		}
	}

	//clock_t start = clock();
	//clock_t end = clock();
	//cout << end-start;
	system("pause");
}