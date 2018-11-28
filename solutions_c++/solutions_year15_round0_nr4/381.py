#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int X, R, C;



bool solve() //true: richard
{
	cin >> X >> R >> C;
	if (R < C)
		swap(R, C);
	if (X >= 7)
		return true;
	if ((R * C) % X != 0)
		return true;
	if (X == 1)
		return false;
	if (X == 2)
	{
		if ((R * C) % 2 == 0)
			return false;
		return true;
	}
	if (X == 3)
	{
		//3*1
		if (3 > R)
			return true;
		//2*2
		if (2 > C)
			return true;
		return false;
	}
	if (X == 4)
	{
		//4*1
		if (4 > R)
			return true;
		//3*2
		if (2 >= C)
			return true;
		return false;
	}
	return false;
}

int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	int T;
	cin >> T;
	for (int case_num = 1; case_num <= T; ++case_num)
	{
		if (solve())
			printf("Case #%d: RICHARD\n", case_num);
		else
			printf("Case #%d: GABRIEL\n", case_num);
	}
	
	return 0;
}

