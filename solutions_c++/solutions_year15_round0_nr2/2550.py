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

#define USEFILE

int getMin(int currentPos, map<int, int> initPans)
{
	int maxPanValue = (*(--initPans.end())).first;
	int maxPanNum = (*(--initPans.end())).second;

	//cout << maxPanValue << " " << maxPanNum << endl;

	if(maxPanValue <= 3)
		return currentPos + maxPanValue;

	int ret = currentPos + maxPanValue;
	for(int a = 1; a <= maxPanValue / 2; a++)
	{
		map<int, int> temp = initPans;

		int b = maxPanValue - a;
		temp.erase(maxPanValue);

		temp[a] += maxPanNum;
		temp[b] += maxPanNum;

		ret = min(ret, getMin(currentPos + maxPanNum, temp));
	}

	return ret;
}

int main(void)
{
#ifdef USEFILE
	FILE* inf = freopen("B.in", "r", stdin);
	FILE* outf = freopen("B_out.txt.", "w", stdout);
#endif

	int tc;
	cin >> tc;

	for(int testNum = 1; testNum <= tc; testNum++)
	{
		int d;
		cin >> d;

		map<int, int> initPans;
		for(int i = 0; i < d; i++)
		{
			int temp;
			cin >> temp;
			initPans[temp]++;
		}

		int ans = getMin(0, initPans);
		printf("Case #%d: %d\n", testNum, ans);
	}


#ifdef USEFILE
	fclose(inf);
	fclose(outf);
#endif

	return 0;
}