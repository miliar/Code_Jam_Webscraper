#include <iostream>
#include <fstream>
#include <streambuf>
#include <iomanip>
#include <time.h>

using namespace std;

int main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");
	int T;
	double C, F, X, f, time;

	streambuf *cin_backup = cin.rdbuf();
	cin.rdbuf(ifs.rdbuf());

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> C >> F >> X;

		f = 2.0;
		time = 0.0;
		while (C/f+X/(f+F) < X/f)
		{
			time += C/f;
			f += F;
		}

		time += X/f;
		ofs << "Case #" << i+1 << ":" << " " << fixed << setprecision(7) << time << endl;;
	}

	cin.rdbuf(cin_backup);

	//clock_t start = clock();
	//clock_t end = clock();
	//cout << end-start;

	system("pause");
}