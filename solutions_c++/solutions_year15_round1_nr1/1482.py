#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

vector<string> &split(const string &s, char delim, vector<string> &elems) {
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}

vector<string> solve_A(vector<string> &inputs)
{
	vector<string> s;
	int case_n = 1;
	int N = stoi(inputs[0]);
	for (int case_n =1; case_n<=N; case_n++)
	{
		int idx = 0;
		int n = stoi(inputs[case_n * 2-1]);
		string tmp_s = inputs[case_n*2];
		int len = 0;
		vector<string> tkns;
		tkns = split(tmp_s, ' ',tkns);

		int m1 = 0;
		int m2 = 0;
		int max_drop = 0;
		int prev = 0;
		int curr = 0;
		for (int i = 0; i<n; i++)
		{
			int curr = stoi(tkns[i]);
			if (curr < prev)
			{
				m1 += prev-curr;
				max_drop = max(max_drop, prev-curr);
			}
			prev = curr;
		}
		prev = 0;
		for (int i = 0; i<n; i++)
		{
			int curr = stoi(tkns[i]);
			if (prev > 0)
			{
				m2 += min(prev, max_drop);
			}
			prev = curr;
		}

		s.push_back("Case #" + to_string(case_n) + ": " + to_string(m1) + " " + to_string(m2));

	}
	return s;
}

int main()
{
	vector<string> inputs;

	ifstream i_file;
	i_file.open("C:\\GJ1A\\1a\\Debug\\inputs\\small.in", ios::in);
	string line;
	if (i_file.is_open())
	{
		while (getline(i_file, line))
		{
			inputs.push_back(line);
		}
		i_file.close();
	}

	vector<string> results;

	results = solve_A(inputs);

	ofstream o_file;
	o_file.open("C:\\GJ1A\\1a\\Debug\\inputs\\small.out", ios::out);
	for (vector<string>::iterator it = results.begin(); it<results.end(); it++)
	{
		o_file << *it;
		if (it + 1<results.end())
		{
			o_file << endl;
		}
	}
	o_file.close();

	return 0;
}