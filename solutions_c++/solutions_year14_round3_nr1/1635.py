#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<numeric>

using namespace std;

typedef struct
{
	unsigned __int64 P;
	unsigned __int64 Q;
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
				auto split_line = split(line, "/");

				p.P = strtoul(split_line[0].c_str(), nullptr, 10);
				p.Q = strtoul(split_line[1].c_str(), nullptr, 10);

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

__int64 solve(PROBLEM &p)
{
	unsigned __int64 qx = p.Q;
	unsigned __int64 px = p.P;
	unsigned long a = 0;

	if (p.Q == 1 && p.P == 1) return 1;

	for (int i = 0; i < 40; ++i)
	{
		if (qx & 1){
			return -1;
		}
		qx /= 2;
		if (qx <= px){
			if (a == 0){
				a = i + 1;
			}
			px -= qx;
			if (px == 0) return a;
		}
	}
	return a;
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
			printf("Case #%d: impossible\n", ++count);
		}
		else
		{
			printf("Case #%d: %lld\n", ++count, x);
		}
	}
	return 0;
}