#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	int num;
	ifstream in("test.in");
	ofstream out("result.out");
	in >> num;
	for (int i = 0; i < num; i++)
	{

		string ret;
		in >> ret;
		int result=1;
		char current;
		current = ret[0];
		for (int j=1;j < ret.length(); j++)
		{
			if (ret[j]!=current)
			{
				result++;
				current = ret[j];
			}
		}
		if (current == '+')
			result--;
		out << "Case #" << i+1 << ": " << result << endl;
	}
	cin.get();
	cin.get();
	return 0;
}