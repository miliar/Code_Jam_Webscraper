#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
using namespace std;

vector<long long> & readFromFile()
{
	vector<long long> * numbers = new vector<long long>();
	ifstream fin ("input.txt");
	int count;
	fin >> count;
	for (int i = 0; i < count; ++i)
	{
		long long curr;
		fin >> curr;
		numbers->push_back(curr);
	}
	return *numbers;

}
void writeResult(vector<long long> & result)
{
	ofstream fout("output.txt");
	for (int i = 0; i < result.size(); ++i)
	{
		if (result[i] == 0 ) fout << "Case #" << i + 1 <<": " << "INSOMNIA" << endl;
		else fout << "Case #" << i + 1 <<": " << result[i] << endl;
	}
}
long long calculate(long long number)
{
	unordered_set<char> s;
	int prev = 0;
	for (int i = 1; i < 10000 && s.size()<10; ++i)
	{
		long long cp = number * i;
		prev = cp;
		while (cp > 0)
		{
			char cur = cp % 10;
			s.insert(cur);
			cp /= 10;
		}
	}
	if (s.size() != 10) return 0;
	else return prev;
}

int main()
{
	auto numbers = readFromFile();
	vector<long long>  result;
	for (auto number: numbers)
	{
		result.push_back(calculate(number));
	}
	writeResult(result);;
	return 0;
}