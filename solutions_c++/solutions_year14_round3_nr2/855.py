#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<list>
#include<set>
#include<algorithm>
#include<cstdio>
#include<numeric>

using namespace std;

typedef struct
{
	std::vector<std::string> C;
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
				getline(ifs, line);
				auto split_line = split(line, " ");

				std::for_each(split_line.begin(), split_line.end(), [&p](const std::string& v)
				{
					p.C.push_back(v);
				});

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

bool valid(const std::string& value)
{
	std::set<char> v;
	std::string v2(value);
	auto end = std::unique(v2.begin(), v2.end());

	for (auto x = v2.begin(); x != end; ++x)
	{
		if (!(v.insert(*x).second)){
			return false;
		}
	}
	return true;
}

__int64 solve_r(const std::vector<std::string>& r, const std::string& value)
{
	if (!valid(value)){
		return 0;
	}
	if (r.size() == 0){
		if (valid(value)) return 1;
		return 0;
	}

	__int64 sum_of_valid = 0;

	for (size_t i = 0; i < r.size(); ++i)
	{
		std::vector<std::string> r2;
		r2.reserve(r.size());
		for (size_t j = 0; j < r.size(); ++j)
		{
			if (i != j){
				r2.push_back(r[j]);
			}
		}
		sum_of_valid += solve_r(r2, value + r[i]);
	}
	return sum_of_valid % 1000000007;
}

__int64 solve(PROBLEM &p)
{
	return solve_r(p.C, std::string());
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

		printf("Case #%d: %lld\n", ++count, x);
	}
	return 0;
}