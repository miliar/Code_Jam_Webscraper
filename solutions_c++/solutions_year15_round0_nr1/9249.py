#include <fstream>
#include <iostream>
#include <string>

using namespace std;


int main()
{
	


	ofstream out("output.txt");
	ifstream in("A-large.in");
	int n, m, ans, tmp;
	string num;
	in >> n;

	for (int j = 0; j < n; j++)
	{
		tmp = 0;
		ans = 0;
		in >> m;
		in >> num;


		for (int i = 1; i < num.length(); i++)
		{
			tmp += num[i - 1] - 48;

			if (tmp < i)
			{
				ans += i - tmp;
				tmp += i - tmp;
			}
		}


		out << "Case #" << j + 1 << ": " << ans << endl;
	}


	return 0;
}


