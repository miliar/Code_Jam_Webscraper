#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int cases;
	in >> cases;
	int num, x, i;
	for (int t = 0; t < cases; t++)
	{
		int y = 1, result;
		bool cond = false;
		in >> num;
		if (num == 0)
		{
			out << "Case #" << t + 1 << ": INSOMNIA";
			if (t != cases - 1)
				out << endl;
			continue;
		}
		int arr[11] = { 0 };
		while (true)
		{
			cond = false;
			x = num * y;
			while (x > 0)
			{
				arr[x % 10]++;
				x /= 10;
			}
			for (int i = 0; i < 10; i++)
			{
				if (arr[i] == 0)
				{
					cond = true;
					break;
				}
			}
			if (!cond)
			{
				result = num * y;
				break;
			}
			y++;
		}
		out << "Case #" << t + 1 << ": " << result;
		if (t != cases - 1)
			out << endl;
	}
	return 0;
}