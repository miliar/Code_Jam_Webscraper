#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <bitset>
#include <climits>
using namespace std;

typedef pair<int, int> pi;
typedef pair<int, string> ps;


vector<string> GetNeighbor(string& input)
{
	vector<string> neighbor;

	for (int i = 0; i != input.size(); ++i)
	{
		string temp;
		string left_half = input.substr(0, (i + 1));

		for (int j = left_half.size()-1; j >= 0; --j)
		{
			(left_half[j] == '+') ? left_half[j] = '-' : left_half[j] = '+';
			temp.push_back(left_half[j]);
		}
		temp += (input.substr(i + 1, input.size() - left_half.size()));
		neighbor.push_back(temp);
	}
	return neighbor;
}


int BFS(string& input)
{
	string end(input.size(), '+');
	if (input == end) 
		return 0;

	queue<string> que;
	unordered_map<string, int> distance;
	que.push(input);
	distance[input] = 0;

	while (!que.empty())
	{
		string curr = que.front();
		que.pop();
		vector<string> neighbor = GetNeighbor(curr);

		for (int i = 0; i != neighbor.size(); ++i)
		{
			if (distance[neighbor[i]] == 0)
			{
				distance[neighbor[i]] = distance[curr] + 1;
				que.push(neighbor[i]);
			}

			if (neighbor[i] == end)
			{
				queue<string> empty;
				que = empty; //break out
			}
		}
	}
	return distance[end];
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	ifstream is; is.open("B-small-attempt0.in");
	ofstream os; os.open("Answer_B_Small.txt");

	int testCase;
	//cin >> testCase;
	is >> testCase;

	for (int i = 0; i != testCase; ++i)
	{
		string input;
		//cin >> input;
		is >> input;
		//cout << "Case #" << (i + 1) << ": " << BFS(input) << endl;
		os << "Case #" << (i + 1) << ": " << BFS(input) << endl;
	}
}