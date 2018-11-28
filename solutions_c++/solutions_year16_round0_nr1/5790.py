#include <vector>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
const int INF = 2147483647;

int main()
{
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for (int times = 1; times <= t; times++)
	{
		vector<bool> has(10, 0);
		int n;
		fin >> n;
		if (n != 0) {
			int num_has = 0;
			int i;
			for (i = 1; num_has < 10; i++)
			{
				int current = i * n;
				int digit;
				while (current > 0)
				{
					digit = current % 10;
					if (!has[digit])
					{
						num_has++;
						has[digit] = true;
					}
					current /= 10;
				}
			}
			fout << "Case #" << times << ": " <<  n*(i - 1) << endl;
		}
		else
			fout << "Case #" << times << ": " << "INSOMNIA" << endl;
	}
	cin.get();
	return 0;
}