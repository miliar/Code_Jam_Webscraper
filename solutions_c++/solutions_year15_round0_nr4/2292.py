#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int x, r, c;

int solve()
{

	if (x == 3 && r == 3 && c == 1)
		return 0;
	if (x == 4 && r == 4 && c == 1)
		return 0;
	if (x == 4 && r == 4 && c == 2)
		return 0;

	if ((r*c) % x != 0)	{
		//cout << "NO 1 " << r*c%x << endl; 
		return 0;
	}
	if (x == 1 && x <= c)	return 1;

	if (x > r){
		//cout << "NO 2" << endl; 
		return 0;
	}
	if (x+1>r+c)
		return 0;

	return 1;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output41.txt", "w", stdout);

	int nTestCase = 0;
	cin >> nTestCase;

	for (int iTestCase = 0; iTestCase < nTestCase; iTestCase++)
	{
		cin >> x >> r >> c;
	 	if (r < c)	swap(r, c);
	// cout << x << " " << r << " " << c << "	";
		if (solve())	cout << "Case #" << iTestCase + 1 << ": GABRIEL" << endl;
		else			cout << "Case #" << iTestCase + 1 << ": RICHARD" << endl;
	 
	}
	return 0;
}