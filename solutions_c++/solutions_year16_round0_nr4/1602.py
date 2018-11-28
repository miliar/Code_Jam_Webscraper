#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());

	ofstream outputfile;
	outputfile.open("Output.txt");

	string line;
	int T = 0, K,C,S;
	ll result;

	vector<ll> numberofFlips;
	char prevChar;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		numberofFlips.resize(T);

		for (int i = 0; i < T; ++i)
		{
			getline(file, line);
			istringstream ss(line);
			
			ss >> K >> C >> S;

			outputfile << "Case #" << i+1 << ": ";

			for (int j = 0; j < K; ++j)
			{
				outputfile << j+1 << " ";
			}
			outputfile << endl;

		}
	}
	
	file.close();

	outputfile.close();

	return 0;
}