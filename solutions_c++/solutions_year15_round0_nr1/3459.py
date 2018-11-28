#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int t = 0;
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("A-large.out",ios::app);
	input >> t;
	for (int i = 0; i < t; i++)
	{
//		if (i == 84)
//			cout << "i = 85" << endl;
		int s = 0;
		input >> s;
		int *s_count = new int[s + 1];
		string audience;
		input >> audience;
		int j = 0;
		for (j = 0; j < s + 1; j++)
		{
			s_count[j] = audience[j] - 48;
		}
		int count = s_count[0];
		int num = 0;
		int count_num = 0;
		for (j = 1; j < s + 1; j++)
		{
			if (s_count[j] == 0)
				continue;
			if (count >= j)
				count += s_count[j];
			else
			{
				num = j - count;
				count = count + num;
				count_num += num;
				count = count + s_count[j];
			}
		}
		output << "Case #"<<i + 1<<": " << count_num << endl;
	}
	return 0;
}