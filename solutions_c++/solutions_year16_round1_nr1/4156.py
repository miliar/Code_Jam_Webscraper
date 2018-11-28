#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <deque>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

#define FOR(i, inPos, endPos) for(int i = int (inPos); i < int (endPos); i++)
#define MAX(i, j) abs(i) < abs(j)? j: i
#define MIN(i, j) abs(int(i)) < abs(int(j))? i: j

int main()
{
	int T = 0;
	cin >> T;

	for (long long i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
		string str = ""; cin >> str;

		string final = "";
		final = str[0];
		for(int j = 1; j < str.size(); j++)
		{
			if(final[0] <= str[j]){ final = str[j] + final;}
			else{ final = final + str[j];}
		}
		cout << final << endl;
	}

	return 0;
}
