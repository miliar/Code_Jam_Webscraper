#include <stdlib.h>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>

typedef std::string Result;

class MultiTable
{
public:
	static MultiTable& Instance()
	{
		static MultiTable s_inst;
		return s_inst;
	}

	int multi(int lhs, int rhs) const
	{
		int ret = _table[abs(lhs) - 'h'][abs(rhs) - 'h'];
		if (lhs < 0) { ret = -ret; }
		if (rhs < 0) { ret = -ret; }
		return ret;
	}

private:
	MultiTable()
	{
		_table.resize(4);
		_table[0].resize(4);
		_table[0][0] = 'h';
		_table[0][1] = 'i';
		_table[0][2] = 'j';
		_table[0][3] = 'k';

		_table[1].resize(4);
		_table[1][0] = 'i';
		_table[1][1] = -1 * 'h';
		_table[1][2] = 'k';
		_table[1][3] = -1 * 'j';

		_table[2].resize(4);
		_table[2][0] = 'j';
		_table[2][1] = -1 * 'k';
		_table[2][2] = -1 * 'h';
		_table[2][3] = 'i';

		_table[3].resize(4);
		_table[3][0] = 'k';
		_table[3][1] = 'j';
		_table[3][2] = -1 * 'i';
		_table[3][3] = -1 * 'h';
	}

	std::vector<std::vector<int> > _table;
};

class ProblemItem
{
public:
	Result solve()
	{
		prepare();
		return solve_one() ? "YES" : "NO";
	}

	bool solve_one()
	{
		int init = 'h';
		for (int i = 0; i < _work.length(); ++i)
		{
			init = MultiTable::Instance().multi(init, _work[i]);
			if (init == 'i')
			{
				//if (i>0 && (i%_repeat == 0))
				{
					//break;
				}
				if (solve_two(i+1))
				{
					return true;
				}
				else { return false; }
			}
		}

		return false;
	}

	bool solve_two(int idx)
	{
		int init = 'h';
		for (int i = idx; i < _work.length(); ++i)
		{
			init = MultiTable::Instance().multi(init, _work[i]);
			if (init == 'j')
			{
				if (solve_last(i+1))
				{
					return true;
				}
				else { return false; }
			}
		}
		return false;
	}

	bool solve_last(int idx)
	{
		int init = 'h';
		for (int i = idx; i < _work.length(); ++i)
		{
			init = MultiTable::Instance().multi(init, _work[i]);
		}
		return init == 'k';
	}

	void prepare()
	{
		std::ostringstream buf;
		for (int i = 0; i < _repeat; ++i)
		{
			buf << _raw;
		}
		_work.swap(buf.str());
	}
	//setter
	void setRepeat(int value)
	{
		_repeat = value;
	}

	void setRaw(const std::string& value)
	{
		_raw = value;
	}

private:
	std::string _work;
	int _repeat;
	std::string _raw;
};

std::vector<ProblemItem> g_item;

void parse_item(FILE* fp)
{
	ProblemItem item;
	char line[20000] = {};
	//do something
	int value;
	fscanf(fp, "%ld", &value);
	int len = value;
	fscanf(fp, "%ld", &value);
	item.setRepeat(value);
	fgets(line, sizeof(line), fp);
	fgets(line, len + 1, fp);
	item.setRaw(line);
	fgets(line, sizeof(line), fp);

	g_item.push_back(item);
};

void solve(const char* file_name)
{
	FILE* fp = fopen(file_name, "wb");
	for (int i = 0; i < g_item.size(); ++i)
	{
		Result rt = g_item[i].solve();
		fprintf(fp, "Case #%ld: %s\n", i + 1, rt.c_str());
	}
	fclose(fp);
}

void parse(const char* file_name)
{
	FILE* fp = fopen(file_name, "rb");
	int value;
	fscanf(fp, "%ld\n", &value);
	for (int i = 0; i < value; ++i)
	{
		parse_item(fp);
	}
	fclose(fp);
}

const char* IN = "c:/work/tmp/input.txt";
const char* OUT = "c:/work/tmp/result.txt";

int main(int argc, char* argv[])
{
	const char* in = argc > 1 ? argv[1] : IN;
	const char* out = argc > 2 ? argv[2] : OUT;
	parse(in);
	solve(out);

	return 0;
}
