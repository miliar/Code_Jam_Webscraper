//Alien Language
//https://code.google.com/codejam/contest/90101/dashboard#s=p0


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <ctime>

#define LARGE_IP
using namespace std;

int main()
{

	auto t = std::time(nullptr);
	auto tm = *std::localtime(&t);
	std::cout << std::put_time(&tm, "Start time : %M:%S") << std::endl;

	ofstream lOutputFile;
#ifdef LARGE_IP
	ifstream lInputFile("A-large-practice.in");
	lOutputFile.open("A-large-practice.out");
#else
	ifstream lInputFile("A-small-practice.in");
	lOutputFile.open("A-small-practice.out");
#endif

	int T = 0;

	lInputFile >> T;
	
	for (int t = 1; t <= T; t++)
	{
		int Smax = 0, ans = 0, cnt = 0;
		string S;

		lInputFile >> Smax >> S;

		for (int i = 0; i <= Smax; i++)
		{
			int Si = S.at(i) - '0';
			cnt += Si;
			if (cnt < (i+1))
			{
				ans++;
				cnt++;
			}
		}
		lOutputFile << "Case #" << t<< ": " << ans << endl;
	}

	lInputFile.close();
	lOutputFile.close();

	t = std::time(nullptr);
	tm = *std::localtime(&t);
	std::cout << std::put_time(&tm, "End Time : %M:%S") << std::endl;
	return 0;
}
