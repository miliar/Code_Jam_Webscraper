#include <iostream>
#include<cstdio>
#include<string>
#include<set>
#include <sstream>
using namespace std;
string IntToString(int number)
{
	ostringstream oss;
	oss << number;
	return oss.str();
}
void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, v, N, temp, temp2, n = 0;
	bool flag;
	string in;
	set<int> asleep;
	cin >> T;
	if (T >= 1 && T <= 100)
	{
		for (int i = 1; i <= T; i++)
		{
			v = 2;
			asleep.clear();
			flag = false;
			cin >> N;
			if (N >= 0 && N <= 1000000)
			{
				n++;
				in = IntToString(N);
				for (int k = 0; k < in.length(); k++)
				{
					temp2 = in[k] - '0';
					asleep.insert(temp2);
				}
				while (!flag)
				{
					for (int j = 0; j < 10;)
					{
						if (asleep.count(j) == 1)
						{
							if (j == 9)
								flag = true;
							j++;
						}
						else
							break;
					}
					if (!flag && v <= 99999)
					{
						temp = N*v;
						in = IntToString(temp);
						for (int b = 0; b < in.length(); b++)
						{
							temp2 = in[b] - '0';
							asleep.insert(temp2);
						}
						v++;
					}
					else if (flag)
					{
						cout << "Case #" << n << ":" << " " << temp << endl;
					}
					else
					{
						flag = true;
						cout << "Case #" << n << ": INSOMNIA" << endl;
					}

				}
			}
		}
	}
	else
		return;
}