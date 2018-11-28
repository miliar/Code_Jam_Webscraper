#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <fstream>
#include <iostream>
#include <limits>

using namespace std;

// runtime 272ms
int countComponents(int n, vector<pair<int, int>>& edges) {
	int res = 0;
	if (n<1) return 0;
	if (n == 1) return 1;

	vector<vector<int>> adjacent(n);
	for (int i = 0; i<edges.size(); i++)
	{
		pair<int, int> edge = edges[i];
		adjacent[edge.first].push_back(edge.second);
		adjacent[edge.second].push_back(edge.first);
	}

	vector<bool> explored(n, false);
	vector<int> connected;
	int p = 0;
	while (p<n)
	{
		if (!explored[p])
		{
			res++;
			explored[p] = true;
			if (!adjacent[p].empty())
			{
				// have adjacent nodes
				connected = adjacent[p];
				while (!connected.empty())
				{
					int node = connected[0];
					connected.erase(connected.begin());
					if (!explored[node])
					{
						explored[node] = true;
						connected.insert(connected.end(), adjacent[node].begin(), adjacent[node].end());
					}

				}
			}
		}
		p++;
	}
	return res;
}

string binaryString(int num)
{
	string res;

	if (!num) res += '0';
	while (num)
	{
		int dig = 1 & num;
		res += dig + '0';
		num >>= 1;
	}
	reverse(res.begin(), res.end());
	return res;
}

int main(int argc, char *argv[])
{
	ifstream inputfile;
	ofstream outputfile;

	// char *inputfilename = argv[2];
	inputfile.open("A-large.in");
	// inputfile.open(inputfilename);
	outputfile.open("output.txt");
	outputfile.clear();

	int cases;
	int count = 1;
	// input case number
	inputfile >> cases;

	int n;
	int sum, dig;
	bool record[10];
	
	while (count <= cases)
	{
		// input n
		inputfile >> n;
		if (n == 0)
		{
			outputfile << "Case #" << count << ": INSOMNIA" << endl;
		}
		else
		{
			sum = 0;
			dig = 0;
			memset(record, false, 10*sizeof(bool));
			while (dig < 10)
			{
				sum += n;
				int temp = sum;
				while (temp)
				{
					int finaldig = temp % 10;
					if (!record[finaldig])
					{
						record[finaldig] = true;
						dig++;
					}
					temp /= 10;
				}
			}
			outputfile << "Case #" << count << ": " << sum << endl;
		}
		count++;
	}
	
	system("pause");
	return 0;
}