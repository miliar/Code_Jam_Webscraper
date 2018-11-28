#include <algorithm>
#include "BigIntegerLibrary.hh"
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

void func(ifstream& in, ofstream& out)
{
	int N, M, o, e, p, s1 = 0, s2 = 0;
	int	cnt[200];
	memset(cnt, 0, sizeof(cnt));
	in >> N >> M;
	for (int i = 0; i < M; i++)
	{
		in >> o >> e >> p;
		for (int j = o; j < e; j++)
			cnt[j] += p;
		s1 += (2 * N - (e - o) + 1) * (e - o) / 2 * p;
	}
	for (int i = 1; i < N;)
	{
		int tmp = 0;
		if (cnt[i] <= 0)
		{
			i++;
			continue;
		}
		for (int j = i; j < N; j++)
		{
			if (cnt[j] > 0)
			{
				tmp++;
				cnt[j]--;
			}
			else
				break;
		}
		s2 += (2 * N - tmp + 1) * tmp / 2;
	}
	out << s1 - s2 << endl;
}

int main()
{
	ifstream in;
	in.open("D:\\code_jam_in.txt");

	ofstream out;
	out.open ("D:\\code_jam_out.txt");
	out << fixed << showpoint << setprecision(7);

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		//cout << "Case #" << t << endl;
		out << "Case #" << t << ": ";
		func(in, out);
	}

	in.close();
	out.close();
	
	return 0;
}