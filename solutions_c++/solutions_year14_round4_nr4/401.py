#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class PairGameEasy
{
public:

	bool dfs(int a, int b, int c, int d)
	{
		if (a == c && b ==d)
		{
			return true;
		}
		if (a > c ||b > d) return false;

		if (dfs(a+b, b, c, d)) return true;
		if (dfs(a, b+a, c, d)) return true;
		return false;
	}

	string able(int a, int b, int c, int d)
	{
		string res;
		if (dfs(a, b, c, d)) res = "Able to generate";
		else res = "Not able to generate";
		return res;
	}

};

int main() {
	PairGameEasy s;
	cout << s.able(1, 2, 3, 4);
	return 0;
}