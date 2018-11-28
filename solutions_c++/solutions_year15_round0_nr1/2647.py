#include <vector>
#include <tuple>
#include <set>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main()
{
	ifstream fin;
	fin.open("A-large.in");
	if (fin.is_open())
	{
		ofstream fout;
		fout.open("A-large.out");
		int T;
		fin >> T;
		for (int i = 0; i < T; i++)
		{
			int N;
			fin >> N;
			string str;
			fin.get();
			getline(fin, str);
			int sum = 0;
			int frnd = 0;
			for (int j = 0; j < N+1; j++)
			{
				if (sum+frnd < j) 
					frnd = j-sum;
				sum += str[j]-'0';

			}
			fout << "Case #" << i + 1 << ": " << frnd << endl;
		}
		fin.close();
		fout.close();
	}
	return 0;
}