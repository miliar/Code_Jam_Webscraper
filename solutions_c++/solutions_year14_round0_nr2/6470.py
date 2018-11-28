#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>
using namespace std;
int main()
{
	ifstream in("in.in");
	ofstream out("out.out");
	long float C, F, X;
	int T;
	in >> T;
	int loop = 1;
	while (T--)
	{
		in >> C >> F >> X;

		long float gainper = 2;//每秒的收入
		long float farmtime = 0;//建农场的花费
		long float pretime = 0;//建n-1农场达到目的时间
		long float nowtime = 0;//现在的时间

		
		for (long int nfarm = 0; nfarm<100000000; nfarm++)//建农场
		{
			nowtime = farmtime + X / gainper;//现在要花的时间
			if (nowtime>pretime && nfarm != 0)
			{
				out << "Case #" << loop << ": " << fixed << setprecision(7) << pretime << endl;
				break;
			}
			farmtime += C / gainper;
			gainper += F;//增加收入
			pretime = nowtime;
		}
		loop++;
	}
	//getchar();
	//getchar();
}