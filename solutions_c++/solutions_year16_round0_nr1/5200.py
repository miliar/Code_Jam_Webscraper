
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <vector>

using namespace std;

class Num
{
public:
	vector<int> val;
	vector<int> initval;

	void print()
	{
		for (int i=val.size()-1; i>=0; --i)
		{
			fout << val[i];
		}
	}

	void init(int v)
	{
		val.clear();
		if (v == 0)
		{
			val.push_back(0);
		}
		else
		{
			while (v != 0)
			{
				int vv = v % 10;
				val.push_back(vv);
				v = v / 10;
			}
		}
		initval = val;
	}

	void go_next()
	{
		for (size_t i=0; i<val.size(); ++i)
		{
			if (i < initval.size())
				val[i] += initval[i];
		}

		int vv;
		for (size_t i=0; i<val.size() - 1; ++i)
		{
			vv = val[i];
			if (vv >= 10)
			{
				val[i] = vv % 10;
				val[i+1] += (vv / 10);
			}
		}
		vv = val[val.size()-1];
		if (vv >= 10)
		{
			val[val.size()-1] = vv % 10;
			val.push_back(vv / 10);
		}
	}
};

class DigitCheck
{
public:
	int appear[10]; // 0 ~ 9

	DigitCheck()
	{
		for (int i=0; i<10; ++i) appear[i] = 0;
	}

	bool check(Num n)
	{
		for (size_t i=0; i<n.val.size(); ++i)
		{
			++appear[n.val[i]];
		}
		int digit_found = 0;
		for (int i=0; i<10; ++i)
		{
			if (appear[i] > 0)
				++digit_found;
		}
		return digit_found == 10;
	}
};

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int N;
		fin >> N;

		Num num;
		num.init(N);

		DigitCheck c;
		bool found = c.check(num);

		if (found)
		{
			fout << "Case #" << cases << ": ";
			num.print();
			fout << endl;
			continue;
		}

		__int64 maxcount = (__int64) pow((double)10, (double)num.val.size()+1)-1;

		for (__int64 i=0; i<maxcount; ++i)
		{
			num.go_next();
			found = c.check(num);

			if (found)
			{
				fout << "Case #" << cases << ": ";
				num.print();
				fout << endl;
				break;
			}
		}

		//fout << "1 : ";
		//num.print();
		//fout << endl;

		//for (int i=2; i<=10; ++i)
		//{
		//	num.go_next();
		//	fout << i << " : ";
		//	num.print();
		//	fout << endl;
		//}

		if (!found)
			fout << "Case #" << cases << ": " << "INSOMNIA" << endl;
	}

	return 0;
}
