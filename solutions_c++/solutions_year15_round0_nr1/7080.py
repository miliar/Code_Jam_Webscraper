#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>


using namespace std;

int main(int argc,char*argv[])
{
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; ++i)
	{
		int smax,
			ans = 0,
			num = 0;
		char s[1005];
		scanf("%d %s",&smax,s);
		for (int i = 0; i <= smax; ++i)
		{
			if(i>num){
				ans += i-num;
				num = i;
			}
			num += s[i]-'0';
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}