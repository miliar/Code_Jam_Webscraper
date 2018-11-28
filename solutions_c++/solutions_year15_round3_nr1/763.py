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

vector<string> solve_template(vector<string> &inputs)
{
	vector<string> s;
	int case_n = 1;
	int N = stoi(inputs[0]);
	for (int case_n = 1; case_n <= N; case_n++)
	{
		int idx = 0;
		long long n = stoll(inputs[case_n]);
		long long res = 1L;
		s.push_back("Case #" + to_string(case_n) + ": " + to_string(res));
	}
	return s;
}

vector<string> solve_A(vector<string> &inputs)
{
	vector<string> s;
	int case_n = 1;
	int N = stoi(inputs[0]);
	for (int case_n = 1; case_n <= N; case_n++)
	{
		vector<string> params;
		params = split(inputs[case_n],' ', params);
		int rows = stoi(params[0]);
		int cols = stoi(params[1]);
		int width = stoi(params[2]);

		int res = 0;
		if (width == 1)
			res = rows*cols;
		else
		{
			res += (rows - 1) * ( cols / width );

			int last_row_tries = cols / width - 1;
			res += last_row_tries;
			res += min(width + 1, cols - last_row_tries*width);
		}
		s.push_back("Case #" + to_string(case_n) + ": " + to_string(res));
	}
	return s;
}

int main()
{
	vector<string> inputs;

	ifstream i_file;
	i_file.open("C:\\GJ1A\\1a\\Debug\\inputs\\input.in", ios::in);
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
	o_file.open("C:\\GJ1A\\1a\\Debug\\inputs\\output.out", ios::out);
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