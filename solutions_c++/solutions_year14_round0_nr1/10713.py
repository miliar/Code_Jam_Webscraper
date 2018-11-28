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
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main ()
{
	freopen("in.txt","r", stdin);
	freopen("out.txt","w", stdout);
	int testcases;
	cin >> testcases;
	for (int t = 0; t < testcases; ++t)
	{
		int answer1, answer2, firstcards[5][5], secondcards[5][5], row1[5], row2[5], counter = 0, number;
		cin >> answer1;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				cin >> firstcards[i][j];
				if (i == answer1 - 1)
					row1[j] = firstcards[i][j];
			}
		}
		cin >> answer2;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				cin >> secondcards[i][j];
				if (i == answer2 - 1)
					row2[j] = secondcards[i][j];
			}
		}
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (row1[i] == row2[j])
					counter++, number = row1[i];
		cout << "Case #" << t+1 << ": ";
		if (counter == 1)
			cout << number << endl;
		else if (counter > 1)
			cout << "Bad magician!\n";
		else
			cout << "Volunteer cheated!\n";
	}
	return 0;
}