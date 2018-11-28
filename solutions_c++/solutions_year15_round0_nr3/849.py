#include <iostream>
#define oo (20000000000000000ll)
#define abs1(x) ((x)>0?(x):(-(x)))
#define sign(x) ((x)>0?1:(-1))
#define min(a,b) ((a)<(b)?(a):(b))
using namespace std;
int mul[5][5] =
{
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2,-1, 4,-3},
	{0, 3,-4,-1, 2},
	{0, 4, 3,-2,-1}
};
int matching[255]={0};

void multi(int &target_sign, int &target_value, int l_sign, int l_value, int r_sign, int r_value)
{
	target_sign = l_sign*r_sign;
	int tmp = mul[l_value][r_value];
	target_sign *= sign(tmp);
	target_value = abs1(tmp);
}

int main()
{
	long long T, l ,x;
	char s[11000];
	long long maxlength;
	long long min_i=oo, min_k=oo;
	int tsign, tvalue;
	int isign, ivalue, ksign, kvalue;
	matching['1'] = 1;
	matching['i'] = 2;
	matching['j'] = 3;
	matching['k'] = 4;
	cin >> T;
	for (int test = 1; test<=T; ++test)
	{
		cout << "Case #" << test << ": ";
		cin >> l >> x;
		cin >> s;
		maxlength = l*x;
		min_i = min_k =oo;
		x %= 4;

		// -- calc total  --
		tsign = tvalue = 1;
		for (int i = 0; i< l; ++i)
		{
			multi(tsign, tvalue, tsign, tvalue, 1, matching[s[i]]);
		}

		int ssign = 1, svalue = 1;
		for (int i = 0; i< x; ++i)
		{
			multi(ssign, svalue, ssign, svalue, tsign, tvalue);
		}

		if (ssign * svalue != -1)
		{
			cout << "NO" << endl;
			continue;
		}

		// -- calc i --
		isign = ivalue = 1;
		for (int i = 0; i< l; ++i)
		{
			multi(isign, ivalue, isign, ivalue, 1, matching[s[i]]);
			int t_isign = isign, t_ivalue = ivalue;
			for (int j = 0; j < 4; ++j)
			{
				if (t_isign == 1 && t_ivalue == matching['i'])
				{
					min_i = min(min_i, l*j + i + 1);
					break;
				}
				multi(t_isign, t_ivalue, tsign, tvalue, t_isign, t_ivalue);
			}
		}

		// -- calc k -- 
		ksign = kvalue = 1;
		for (int i = l-1; i >= 0; --i)
		{
			multi(ksign, kvalue, 1, matching[s[i]], ksign, kvalue);
			int t_ksign = ksign, t_kvalue = kvalue;
			for (int j = 0; j < 4; ++j)
			{
				if (t_ksign == 1 && t_kvalue == matching['k'])
				{
					min_k = min(min_k, l*j + l - i);
					break;
				}
				multi(t_ksign, t_kvalue, t_ksign, t_kvalue, tsign, tvalue);
			}
		}

		if (min_i + min_k < maxlength)
		{
			cout << "YES" << endl;
		}
		else
		{
			cout << "NO" << endl;
		}

	}
	return 0;
}
