#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;
vector<long long int> mark;
vector<vector<long long int> >a;
long long cnt;

using namespace std;
int main()
{
#ifdef _DEBUG
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
#endif

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		int Smax;
		string inp;

		cin >> Smax >> inp;

		int current = 0 + inp[0] - '0';
		int answer = 0;
		for (int j = 1; j < inp.length(); j++)
		{
			int sValue = inp[j] - '0';
			if (j > current && sValue > 0)
			{
				int extra = j - current;
				answer += extra;
				current += extra;
			}
			current += sValue;
		}
		printf("Case #%d: %d\n",i,answer);
	}

	return 0;
}