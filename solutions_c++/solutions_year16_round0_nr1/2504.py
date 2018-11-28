#include <iostream>
#include <fstream>
#include <set>
#define LL long long
#define MAXN 1000000
using namespace std;

int hash_arr[10];

LL max(LL x, LL y)
{
	return x > y ? x : y;
}

void getNum(LL x)
{
	while (x)
	{
		int d = x % 10;
		hash_arr[d] = 1;
		x /= 10;
	}
}

bool judge()
{
	for (int i = 0; i < 10; i++)
	{
		if (!hash_arr[i])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	fstream fin("in.txt");
	fstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++ )
	{
		LL N;
		fin >> N;
		memset(hash_arr, 0, sizeof(hash_arr));
		LL i = 1, res = 0;
		for ( ; i <= MAXN; i++)
		{
			getNum( i * N );
			if (judge())
			{
				res = max( i*N, res );
				break;
			}
		}
		if (res == 0)
		{
			fout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else
		{
			fout << "Case #" << t << ": " << res << endl;
		}
	}
	return 0;
}