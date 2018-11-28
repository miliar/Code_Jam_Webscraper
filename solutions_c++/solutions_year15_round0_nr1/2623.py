#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;

int main(void)
{
	FILE* inf = freopen("A.in", "r", stdin);
	//FILE* inf = freopen("sample.txt", "r", stdin);
	FILE* outf = freopen("a_out.txt.", "w", stdout);

	int tc;
	cin >> tc;

	for(int tcNum = 1; tcNum <= tc; tcNum++)
	{
		int n;
		cin >> n;

		string people;
		cin >> people;

		int ans = 0;
		int curPeople = 0;
		for(int i = 0; i < people.size(); i++)	// ith level
		{	
			if(curPeople < i)
			{	
				ans += i - curPeople;
				curPeople = i;
			}

			int peopleNum = people[i] - '0';
			curPeople += peopleNum;
		}

		printf("Case #%d: %d\n", tcNum, ans);
	}


	return 0;
}
