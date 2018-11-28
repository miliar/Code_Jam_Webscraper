
#define PROBLEM_NAME "C"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>

#define v_1 0
#define v_i 1
#define v_j 2
#define v_k 3

int quat_val[4][4] =
{
	{ v_1, v_i, v_j, v_k },
	{ v_i, v_1, v_k, v_j },
	{ v_j, v_k, v_1, v_i },
	{ v_k, v_j, v_i, v_1 }
};

int quat_sign[4][4] =
{
	{ 1, 1, 1, 1},
	{ 1, -1, 1, -1},
	{ 1, -1, -1, 1},
	{1, 1, -1, -1}
};

inline pair<int, int> init(char ch)
{
	if (ch == 'i')
		return make_pair(1, v_i);
	else if (ch == 'j')
		return make_pair(1, v_j);
	else // if (ch == 'k')
		return make_pair(1, v_k);
}

inline pair<int, int> mul(pair<int, int> a, pair<int, int> b)
{
	int sign = quat_sign[a.second][b.second] * a.first * b.first;
	int val = quat_val[a.second][b.second];
	return make_pair(sign, val);
}

// sign, val
pair<int, int> subval(const vector<pair<int, int> >& str, int begin, int end)
{
	pair<int, int> rval = make_pair(1, v_1);
	for (int i=begin; i<end; ++i)
	{
		rval = mul(rval, str[i]);
	}
	return rval;
}


int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int L, X;
		fin >> L >> X;
		string str;
		fin >> str;

		string s = str;
		for (int i=1; i<X; ++i)
			s += str;

		vector<pair<int, int> > value;
		for (int i=0; i<L*X; ++i)
		{
			value.push_back(init(s[i]));
		}

		bool found = false;

		pair<int, int> val_i = make_pair(1, v_1);
		int idx = 0;
		for (idx=0; idx<L*X; ++idx)
		{
			val_i = mul(val_i, value[idx]);
			if (val_i.first == 1 && val_i.second == v_i)
			{
				break;
			}
		}
		if (idx < L*X-2)
		{
			pair<int, int> val_k = make_pair(1, v_1);
			bool found_k = false;

			int ridx = L*X-1;
			for (; idx+2 <= ridx; --ridx)
			{
				val_k = mul(value[ridx], val_k);
				if (val_k.first == 1 && val_k.second == v_k)
				{
					found_k = true;
					break;
				}
			}

			if (found_k)
			{
				pair<int, int> is_j = subval(value, idx+1, ridx);
				if (is_j.first == 1 && is_j.second == v_j)
				{
					found = true;
				}
			}
		}

		//for (int i=1; i<L*X-1 && !found; ++i)
		//{
		//	pair<int, int> is_i = subval(value, 0, i);
		//	if (is_i.first == 1 && is_i.second == v_i)
		//	{
		//		for (int j=i+1; j<L*X; ++j)
		//		{
		//			pair<int, int> is_j = subval(value, i, j);
		//			if (is_j.first == 1 && is_j.second == v_j)
		//			{
		//				pair<int, int> is_k = subval(value, j, L*X);
		//				if (is_k.first == 1 && is_k.second == v_k)
		//				{
		//					found = true;
		//					break;
		//				}
		//			}
		//		}
		//	}
		//}

		fout << "Case #" << cases << ": " << (found ? "YES" : "NO") << endl;
	}

	return 0;
}
