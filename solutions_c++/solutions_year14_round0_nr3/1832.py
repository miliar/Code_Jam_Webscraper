#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>

using namespace std;

typedef struct
{
	unsigned __int64 R;
	unsigned __int64 C;
	unsigned __int64 M;
}PROBLEM;

vector<string> split(const string& line, const string& sep)
{
	int pos[2];
	pos[0] = pos[1] = 0;
	vector<string> split_line;
	while ((pos[1] = line.find(sep, pos[0])) != string::npos)
	{
		string sub_line = line.substr(pos[0], pos[1] - pos[0]);
		split_line.push_back(sub_line);
		pos[0] = pos[1] + 1;
	}
	string sub_line = line.substr(pos[0]);
	split_line.push_back(sub_line);
	return split_line;
}

bool read_problem(const char *fname, vector<PROBLEM>& problems)
{
	fstream ifs;
	ifs.open(fname);

	if (!ifs.is_open()) return false;

	int T = 0;
	try{
		std::string line;
		int line_num = 0;
		while (getline(ifs, line)){
			if (line_num == 0)	{
				T = strtoul(line.c_str(), NULL, 10);
			}
			else{
				PROBLEM p;
				auto split_line = split(line, " ");

				p.R = strtoul(split_line[0].c_str(), nullptr, 10);
				p.C = strtoul(split_line[1].c_str(), nullptr, 10);
				p.M = strtoul(split_line[2].c_str(), nullptr, 10);

				problems.push_back(p);
			}
			++line_num;
		}
	}
	catch (...){
		return false;
	}
	if (problems.size() != T) return false;
	return true;
}


bool check(const PROBLEM &p, int i, int j)
{
	return (i >= 0 && j >= 0 && p.R > i && p.C > j);
};


int open(const PROBLEM &p, char b[11][11], int i, int j)
{
	int count = 0;
	const int direction[8][2] =
	{ { -1, -1 }, { 0, -1 }, { 1, -1 },
	{ -1, 0 }, { 1, 0 },
	{ -1, 1 }, { 0, 1 }, { 1, 1 } };
	for (int d = 0; d < 8; ++d)
	{
		bool c = check(p, i + direction[d][0], j + direction[d][1]);
		if (c) {
			auto& po = b[i + direction[d][0]][j + direction[d][1]];
			if (po == '*') {
				po = '.';
				++count;
			}
		}
	}
	return count;
};

bool solve_r(const PROBLEM &p, char b[11][11], int i, int j)
{
	int count = 0;
	for (int x = 0; x < p.R; ++x)
	{
		for (int y = 0; y < p.C; ++y)
		{
			if (b[x][y] == '*') ++count;
		}
	}
	if (count == p.M) return true;
	if (count < p.M) return false;

	const int direction[8][2] =
	{ { -1, -1 }, { 0, -1 }, { 1, -1 },
	{ -1, 0 }, { 1, 0 },
	{ -1, 1 }, { 0, 1 }, { 1, 1 } };

	for (int d = 0; d < 8; ++d)
	{
		if (check(p, i + direction[d][0], j + direction[d][1]))
		{
			char temp[11][11];
			memcpy(temp, b, 11 * 11);
			int c = open(p, temp, i + direction[d][0], j + direction[d][1]);

			if (c != 0 && solve_r(p, temp, i + direction[d][0], j + direction[d][1]))
			{
				memcpy(b, temp, 11 * 11);
				return true;
			}

		}
	}
	return false;
};

std::string solve(const PROBLEM &p)
{
	auto Impossible = []() { return "Impossible";  };

	int x = (p.R * p.C) - p.M;

	if (x == 0) return Impossible();

	char B[11][11];
	for (int i = 0; i < 11; ++i)
	{
		for (int j = 0; j < 11; ++j)
		{
			if (check(p, i, j))
			{
				B[i][j] = '*';
			}
			else{
				B[i][j] = '\0';
			}
		}
	}

	B[0][0] = 'c';
	if (x != 1)
	{
		open(p, B, 0, 0);
	}
	if (solve_r(p, B, 0, 0)){
		std::string a;
		for (int s = 0; s < p.R; ++s)
		{
			for (int t = 0; t < p.C; ++t)
			{
				a.push_back((char)B[s][t]);
			}
			if (s != p.R - 1) a.push_back('\n');
		}
		return a;
	}

	return Impossible();
}

int main(int argc, char *argv[])
{
	vector<PROBLEM> problems;
	if (argc != 2) return -1;
	if (!read_problem(argv[1], problems)) return -2;

	int count = 0;
	for (auto itr = problems.begin(); itr != problems.end(); ++itr)
	{
		PROBLEM &problem = *itr;

		auto x = solve(problem);

		printf("Case #%d:\n%s\n", ++count, x.c_str());
	}
	return 0;
}