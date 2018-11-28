#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>

#include <iostream>

//#include <cctype>
#include <cmath>

#include <fstream>

using namespace std;

string SolveCaseLLL()
{
	const char * STR_YES = "YES";
	const char * STR_NO  = "NO";

	int a[100][100] = {0};
	
	int N = 0;
	int M = 0;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> a[i][j];
		}
	}

	//cout << endl << "-------------------------------" << endl;
	//for (int i = 0; i < N; i++)
	//{
	//	for (int j = 0; j < M; j++)
	//	{
	//		cout << a[i][j] << "   ";
	//	}
	//	cout << endl;
	//}


	if ((1==N) || (1==M)) return STR_YES;


	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			int flag1 = 0;
			int flag2 = 0;
			int flag3 = 0;
			int flag4 = 0;

			for (int k = 0; k < i; k++)
			{
				if (a[k][j] > a[i][j]) flag1 = 1;
			}

			for (int k = i+1; k < N; k++)
			{
				if (a[k][j] > a[i][j]) flag2 = 1;
			}

			for (int k = 0; k < j; k++)
			{
				if (a[i][k] > a[i][j]) flag3 = 1;
			}

			for (int k = j+1; k < M; k++)
			{
				if (a[i][k] > a[i][j]) flag4 = 1;
			}

			if ((flag1 + flag2 > 0) && (flag3 + flag4 > 0))  return STR_NO;

		}
	}

	return STR_YES;
}

void LLL()
{
	char line[10] = {0};
	cin.getline(line,10);
	
	int testCases = atoi(line);
	for(int i = 0; i < testCases; ++i)
	{
		cout << "Case #" << (i + 1) << ": " << SolveCaseLLL();
		cout << endl;
	}
}


//-----------------------------------------------------------------------------------------------//
//----- main function ---------------------------------------------------------------------------//
//-----------------------------------------------------------------------------------------------//
int main()
{
	TTT();
	return 0;
}
