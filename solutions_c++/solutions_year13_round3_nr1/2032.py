#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int i = 0; i < T; ++i)
	{
		char temp[1000];
		int n, result = 0;
		fin >> temp >> n;
		string name = temp;
		
		int curCon = 0;

		for (int j = n; j <= name.size(); ++j) // size
		{
			for (int s = 0; s <= name.size() - j; ++s) // cur sector
			{
				for (int k = 0; k < j; ++k) // move
				{
					if (name[k + s] != 'a' && name[k + s] != 'e' && name[k + s] != 'i' && name[k + s] != 'o' && name[k + s] != 'u')
						curCon++;
					else if (curCon >= n)
					{
						result++;
						break;
					}
					else
					{
						curCon = 0;
					}
					if (curCon >= n)
					{
						result++;
						break;
					}
				}
				curCon = 0;
			}
		}
		//a, e, i, o, and u

		fout << "Case #" << i + 1 << ": " << result << endl;
	}

	fin.close();
	fout.close();

	return 0;
} 