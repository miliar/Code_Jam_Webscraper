#include <stdlib.h>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>

typedef int Result;

struct Barber
{
	static bool sort_by_time(const Barber& lhs, const Barber& rhs)
	{
		if (lhs._work_time == rhs._work_time)
		{
			return lhs._seq < rhs._seq;
		}
		return lhs._work_time < rhs._work_time;
	}

	static bool sort_by_seq(const Barber& lhs, const Barber& rhs)
	{
		return lhs._seq < rhs._seq;
	}

	int _seq;
	int _work_time;
};

class ProblemItem
{
public:
	Result solve()
	{
		init();
		prepare();

		return solve_one();
	}

	void init()
	{
		for (int i = 0; i < _barbers.size(); ++i)
		{
			Barber barber;
			barber._seq = i + 1;
			barber._work_time = _barbers[i];
			_idle.push_back(barber);
		}
	}

	void prepare()
	{
		int result = 1;
		for (int i = 0; i < _barbers.size(); ++i)
		{
			result = lcm(result, _barbers[i]);
		}
		int mod = 0;
		for (int i = 0; i < _barbers.size(); ++i)
		{
			mod += result / _barbers[i];
		}
		_n = (_n-1)%mod;
	}

	int solve_one()
	{
		int ret;
		int seq = 0;
		while(true)
		{
			if (_idle.size()>0)
			{
				if (seq == _n)
				{
					ret = _idle[0]._seq;
					break;
				}
				_busy.push_back(_idle[0]);
				_idle.erase(_idle.begin());
				++seq;
			}
			else
			{
				std::sort(_busy.begin(), _busy.end(), Barber::sort_by_time);
				int erase_end = 0;
				int time_to_cut = _busy[0]._work_time;
				for (int i = 0; i < _busy.size(); ++i)
				{
					_busy[i]._work_time -= time_to_cut;
					if (_busy[i]._work_time == 0)
					{
						Barber barber = _busy[i];
						barber._work_time = _barbers[barber._seq - 1];
						_idle.push_back(barber);
						erase_end = i;
					}
				}
				_busy.erase(_busy.begin(), _busy.begin()+erase_end + 1);
			
				std::sort(_idle.begin(), _idle.end(), Barber::sort_by_seq);
			}
		}
		return ret;
	}

	//setter
	void addBarber(int value)
	{
		_barbers.push_back(value);
	}

	void setN(int value)
	{
		_n = value;
	}
private:
	static int lcm(int x, int y)
	{
		return (x * y / gcd(x, y));
	}

	static int gcd(int x, int y)
	{
		int r;
		while ((r = x % y) != 0)
		{
			x = y;
			y = r;
		}
		return y;
	}

	std::vector<int> _barbers;
	int _n;

	std::vector<Barber> _idle;
	std::vector<Barber> _busy;
};

std::vector<ProblemItem> g_item;

void parse_item(FILE* fp)
{
	ProblemItem item;
	char line[2000] = {};
	int value;
	fscanf(fp, "%ld", &value);
	int count = value;
	fscanf(fp, "%ld", &value);
	item.setN(value);
	fgets(line, sizeof(line), fp);
	for (int i = 0; i < count; ++i)
	{
		fscanf(fp, "%ld", &value);
		item.addBarber(value);
	}
	fgets(line, sizeof(line), fp);
	//do something

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
