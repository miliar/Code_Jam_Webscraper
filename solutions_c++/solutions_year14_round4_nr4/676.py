// Codejam2014_1C.cpp : Defines the entry point for the console application.
//


#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#ifdef __GNUC__
#include  <tr1/unordered_map>
#define unordered_map tr1::unordered_map
#else
#include <unordered_map>
#endif

using namespace std;


#define F(vec, index) for (int index = 0; index  < vec.size(); ++index)
#define F_S(vec, index, start) for (int index = start; index  < vec.size(); ++index)


//void swapFromTo (vector<int>& copyData, int from, int to)
//{
//}
int maxNode;
int maxNodeCount;

set<string> s;

int GetNode(vector<string> data)
{
	s.clear();
	F(data, j)
	for (int i = 0; i <= data[j].size(); ++i)
	{
		string str = data[j].substr(0, i);
		s.insert(str);
	}
	
	return s.size();
}

void rec(int N, vector<string>& data, int currI, vector<int>& assigment)
{
	if (currI >= assigment.size())
	{
		int currNode = 0;
		for (int j = 0; j < N; ++j)
		{
			vector<string> dataForTry;
			F(assigment, k)
			{
				if (assigment[k] == j)
					dataForTry.push_back(data[k]);
			}
			currNode += GetNode(dataForTry);
		}
		

		if (maxNode < currNode)
		{
			maxNode = currNode;
			maxNodeCount = 1;
		}
		else if (maxNode == currNode)
		{
			maxNodeCount++;
		}
		
		
		return;
	}
	for (int j = 0; j < N; ++j)
	{
		assigment[currI] = j;
		rec(N, data, currI + 1, assigment);
	}

	
}

int main(int argc, char* argv[])
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		
		//std::cout << t << endl;
		int M, N = 0;

		cin >> M >> N;

		vector<string> data(M);

		F(data, i)
		{
			cin >> data[i];
		}
		vector<int> assigment(data.size(), -1);

		maxNode = -1;
		maxNodeCount = 0;

		rec(N, data, 0, assigment);

		cout << "Case #" << t + 1 << ": "  << maxNode << " " << maxNodeCount << endl;
	}

	return 0;
}
