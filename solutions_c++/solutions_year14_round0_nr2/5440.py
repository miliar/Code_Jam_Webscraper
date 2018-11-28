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
	long double C;
	long double F;
	long double X;
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

				p.C = strtold(split_line[0].c_str(), nullptr);
				p.F = strtold(split_line[1].c_str(), nullptr);
				p.X = strtold(split_line[2].c_str(), nullptr);

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

long double solve(const PROBLEM &p)
{
	long double cps = 2.0;
	long double ready= 0;
	long double val = p.X / cps;
	while (true)
	{
		ready += p.C / cps;
		cps += p.F;	
		if (val <= ready + (p.X / cps)){
			return val;
		}
		val = ready + (p.X / cps);
	}
	return 0.0;
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

		printf("Case #%d: %.7Lf\n", ++count, x);
	}
	return 0;
}