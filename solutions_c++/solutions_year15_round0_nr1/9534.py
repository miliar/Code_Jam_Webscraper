#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int standingOvation(int maxShy, string str)
{
	//int result=-1;
	int count = 0;
	int trivial = 0;
	for (int i = 1; i <= maxShy; i++)
	{
		int tmp = 0;
		for (int j = 0; j < i; j++)
		{
			tmp += int(str[j] - '0');
		}
		if (str[i] != '0'&&tmp + trivial < i)
		{
			count += i - (tmp + trivial);
			trivial += i - (tmp + trivial);
			//str[0] += int(str[i] - '0') - tmp;
		}
	}
	return count;

	/*for (int i = 0; i < maxShy; i++)
	{
	count += int(str[i] - '0');
	}
	return (maxShy-count<=0?0:maxShy-count);*/
}

int main()
{
	ofstream out1("D:\\out.txt");
	ifstream in1("D:\\A-small-attempt1.in");
	//ifstream in1("D:\\practice_in.in"); 
	int tnum = -1;
	in1 >> tnum;
	int maxTnum = tnum;
	while (tnum > 0)
	{
		tnum--;
		int maxShy = -1;
		string str;
		in1 >> maxShy;
		in1 >> str;
		out1 << "Case #" << maxTnum - tnum << ": " << standingOvation(maxShy, str) << endl;
	}
}