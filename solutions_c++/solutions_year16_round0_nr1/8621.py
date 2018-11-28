#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdint.h>
#include <cstdio>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;

	in.open("A-large.in");
	out.open("A-large.txt");

	int cnt = 1, TestCase;

	in >> TestCase;
	//cin >> TestCase;

	while (TestCase--)
	{
		string str; 
		int64_t num, chk, ret, tmp, N; 
		int count[10]; 
		for (int a = 0; a < 10; a++) count[a] = 0;

		in >> num;
		//cin >> num;
		chk = 999999;
		N = 1;
		bool bRet = false;

		while (chk >= 0)
		{
			bRet = false;
			ret = num * N; 
			tmp = ret;
			// count digits 
			while (tmp > 0)
			{
				count[tmp % 10] = 1;
				tmp /= 10;
			}
			chk--;
			int b = 0;
			for (int a = 0; a < 10; a++)
			{
				if (count[a] == 1) b++;
			}

			if (b == 10)
			{
				bRet = true;
				break;
			}
			N++;
		}

		if (bRet == false) str = "INSOMNIA";
		else str = to_string(ret);

		cout << "Case #" << cnt << ": " << str << endl;
		out << "Case #" << cnt++ << ": " << str << endl;
	}
	out.close();
	in.close();

	return 0;
}