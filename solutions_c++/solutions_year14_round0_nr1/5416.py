#include<stdio.h>
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
	int C[2][4][4];
	int V[2];
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

				for (int j = 0; j < 2; ++j)
				{
					if(j)getline(ifs, line);
					p.V[j] = _strtoi64(line.c_str(), NULL, 10);
					for (int i = 0; i < 4; ++i)
					{
						getline(ifs, line);
						auto split_line = split(line, " ");

						for (int t = 0; t < 4; ++t)
						{
							auto split_line = split(line, " ");
							p.C[j][i][t] = _strtoi64(split_line[t].c_str(), NULL, 10);
						}
					}
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
	std::set<int> F(&(p.C[0][p.V[0]-1][0]), &(p.C[0][p.V[0]-1][4]));
	std::set<int> S(&(p.C[1][p.V[1]-1][0]), &(p.C[1][p.V[1]-1][4]));
	std::vector<int> I;
	std::set_intersection(F.begin(), F.end(), S.begin(), S.end(), std::back_inserter(I));

	if (I.size() == 0){
		return -1;
	}
	if (I.size() != 1){
		return 0;
	}
	return I[0];
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
			printf("Case #%d: Volunteer cheated!\n", ++count, x);
		}
		else if (x == 0){
			printf("Case #%d: Bad magician!\n", ++count, x);
		}
		else{
			printf("Case #%d: %d\n", ++count, x);
		}
	}
	return 0;
}