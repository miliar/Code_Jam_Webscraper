#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<vector<int>> readFromFile()
{
	vector<vector<int>> input (0, vector<int>(0));
	ifstream fin ("input.txt");
	int count;
	fin >> count;
	string s;
	getline(fin, s);	
	for (int i = 0; i < count; ++i)
	{
		vector<int> cur;
		getline(fin, s);
		for (auto ch : s)
		{
			if (ch == '-') cur.push_back(0);
			if (ch == '+') cur.push_back(1);
		}
		input.push_back(cur);
	}
	return input;

}
void writeResult(vector<int> & result)
{
	ofstream fout("output.txt");
	for (int i = 0; i < result.size(); ++i)
	{
		 fout << "Case #" << i + 1 <<": " << result[i] << endl;
	}
}
void showvector(vector<int> v)
{
	for (auto elem : v)
	{
		cout << elem << " ";
	}
	cout << endl;
}

int count (vector<int> pancakes)
{
	int count = 0;
	while (!pancakes.empty())
	{
		while (pancakes[pancakes.size() -1] == 1)
		{
			pancakes.pop_back();
		}
		if (pancakes.size() > 0) count++;
		for (int i = 0; i < pancakes.size(); ++i)
		{
			if (pancakes[i]) pancakes[i] = 0;
			else pancakes[i] = 1;
		}
	}

	return count;

}

int main()
{
	auto tests = readFromFile();
	vector<int> result;
	for (auto elem :tests)
	{
		int cur = count(elem);
		result.push_back(cur);
	}
	writeResult(result); 
	return 0;
}