#include <stdlib.h>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>

typedef int Result;

class ProblemItem
{
public:
	Result solve()
	{
		int ret = 0;
		int total = _audience[0];
		for (int i = 1; i < _audience.size(); ++i)
		{
			if (total < i)
			{
				ret += (i - total);
				total = i;
			}
			total += _audience[i];
		}

		return ret;
	}

//setter
	void addAudience(int value)
	{
		_audience.push_back(value);
	}
private:
	std::vector<int> _audience;
};
std::vector<ProblemItem> g_item;

void parse_item(FILE* fp)
{
	ProblemItem item;
	char line[2000] = {};
	//do something
	int value;
	fscanf(fp, "%ld", &value);
	fgetc(fp);
	int count = value;
	for (int i = 0; i < count+1; ++i)
	{
		value = fgetc(fp);
		item.addAudience(value - '0');
	}
	fgets(line, sizeof(line), fp);
	
	g_item.push_back(item);
};

void solve(const char* file_name)
{
	FILE* fp = fopen(file_name, "wb");
	for (int i = 0; i < g_item.size(); ++i)
	{
		Result rt = g_item[i].solve();
		fprintf(fp, "Case #%ld: %ld\n", i + 1, rt);
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
