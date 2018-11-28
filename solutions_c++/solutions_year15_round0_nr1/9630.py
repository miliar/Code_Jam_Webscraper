#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream input("A-small-attempt1.in");
	ofstream output("output.txt");
	int num, max, count, addition;
	string maxS;
	input >> num;
	for (int n = 0; n < num; n++)
	{
		output << "Case #" << n + 1 << ": ";
		input >> max >> maxS;
		count = 0;
		addition = 0;
		for (int i = 0; i <= max; i++)
		{
			if (count < i && maxS[i] > 48)
			{
				addition += i - count;
				count += addition;
			}
			int curr = maxS[i] - 48;
			count += curr;
		}
		output << addition << endl;
	}
}