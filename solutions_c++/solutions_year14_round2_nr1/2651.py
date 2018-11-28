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
	std::vector<std::string> S;
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
				int N = strtoul(line.c_str(), nullptr, 10);

				for (int i = 0; i < N; ++i)
				{
					getline(ifs, line);
					p.S.push_back(line);
				}
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

int solve(PROBLEM &p)
{
	std::string x;
	
	for (int i = 0; i < p.S.size(); ++i)
	{
		std::string xa;
		char c = 0;
		for (int j = 0; j < p.S.at(i).size(); ++j)
		{
			if (p.S.at(i).at(j) != c){
				xa.push_back(p.S.at(i).at(j));
				c = p.S.at(i).at(j);
			}
		}
		if (i == 0) x = xa;
		else if (x != xa) return -1;
	}
	std::vector<int> I(p.S.size(), 0);

	int total = 0;
	for (int i = 0; i < x.length(); ++i)
	{
		char s = x.at(i);
		std::vector<int> t(p.S.size(), 0);
		int c = 0;
		for (int j = 0; j < p.S.size(); ++j)
		{
			int co = 0;
			while (I.at(j) < p.S.at(j).length() && p.S.at(j).at(I.at(j)) == s){
				++I.at(j); ++co;
			}
			if (co == 0) {
				return -1;
			}
			t.at(j) = co;
			c += co;
		}
		int x2 = 0;
		int h = c / p.S.size();
		for (int j = 0; j < p.S.size(); ++j)
		{
			x2 += t.at(j) > h ? t.at(j) - h : h - t.at(j);
		}
		total += x2;
	}

	return total;
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

		if (x == -1)
		{
			printf("Case #%d: Fegla Won\n", ++count);
		}
		else
		{
			printf("Case #%d: %d\n", ++count, x);
		}
	}
	return 0;
}