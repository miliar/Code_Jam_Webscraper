#include <vector>
#include <list>
#include <map>
#include <set>
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

int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int T;

	scanf("%d", &T);
	for (int i=1;i<=T;i++) 
	{
		char str[1002] = {0};
		int smax = 0;
		scanf("%d", &smax);
		scanf("%s",str);
		int cnt = 0;
		int smem = 0;
		for(int j = 0; j < smax+1; j++)
		{
			if(j > smem)
			{
				smem++;
				cnt++;
			}
			smem += (str[j] - '0');
		}
		printf("Case #%d: ", i);
		printf("%d\n", cnt);
	}
	return 0;
}
