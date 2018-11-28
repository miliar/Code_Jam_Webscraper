#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <fstream>

using namespace std;

vector<long long int> num_list;

bool judge_num(long long num)
{
	char str[100] = "\0";
	sprintf(str, "%lld", num);
	int len = strlen(str);
	for (int i=0; i < len; i++)
	{
		if (str[i] != str[len-i-1])
			return false;
	}

	return true;
}
int bisearch_left(long long int a)
{
	int l = 0;
	int r = num_list.size();
	
	while (l <= r)
	{
		int m = (l+r)/2;
		if (a < num_list[m])
		{
			r = m-1;
		}
		else if (a == num_list[m])
		{
			return m;
		}
		else 
		{
			l = m+1;
		}
	}
	return l;
}
int bisearch_right(long long int b)
{
	int l = 0;
	int r = num_list.size();
	
	while (l <= r)
	{
		int m = (l+r)/2;
		if (b < num_list[m])
		{
			r = m-1;
		}
		else if (b == num_list[m])
		{
			return m;
		}
		else 
		{
			l = m+1;
		}
	}
	return r;
}
int main()
{
	ofstream fout;
	ifstream fin;
	fin.open("in.in");
	fout.open("A_small.txt");
	int T;
	long long int limit = 100000000000000; // 10^14
	long long int limit_sq = 10000001; // 10^7
	num_list.clear();
	for (long long int i=1; i<=limit_sq; i++)
	{
		long long int num = i * i;
		if (judge_num(num) == true &&
			judge_num(i) == true)
		{
			num_list.push_back(num);
		}
	}
	// cin >> T;
	fin >> T;
	for (int cases = 1; cases<=T; cases++)
	{
		long long int A, B;
		// cin >> A >> B;
		fin >> A >> B;
		long long int cnt = 0;
		long long l = bisearch_left(A);
		long long r = bisearch_right(B);
		cnt = r - l + 1;
		fout << "Case #" << cases << ": " << cnt << endl;
	}
	fout.close();
	fin.close();
	system("pause");
	return 1;
}