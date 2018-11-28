#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <fstream>
using namespace std;
int main()
{
	ifstream input;
	ofstream output;
	input.open("A-small-attempt0.in");
	output.open("A-small-attempt0.on");
	int T;
	input >> T;
	for (int i = 0; i < T; i++)
	{
		int number = 0;
		input >> number;
		if (number == 0)
		{
			output << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		int N = 1;
		double tmp = 0;
		string d;
		map<char, int> dic;
		map<char, int>::iterator it;
		while (true)
		{
			tmp = N * number;
			ostringstream strs;
			strs << tmp;
			d = strs.str();
			//d = to_string(tmp);
			for (int x = 0; x < d.length(); x++)
			{
				it = dic.find(d[x]);
				if (it != dic.end())
				{
					dic[d[x]]++;
				}
				else
				{
					dic[d[x]] = 1;
				}
			}
			if (dic.size() == 10)
			{
				output << "Case #" << i + 1 << ": " << tmp;
				if (i != T-1) output << endl;
				break;
			}
			N++;
		}

	}
	return 0;
}
