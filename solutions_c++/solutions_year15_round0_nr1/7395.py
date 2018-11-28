#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

int TC;
int S,cnt=1;
char tab[1005];

int main()
{
	scanf("%d",&TC);
	while(TC--)
	{
		scanf("%d %s",&S,tab);
		int tot = 0;
		int inv = 0;
		for (int i = 0; i <= S; ++i)
		{
			if(i > tot)
			{
				inv += abs(tot-i);
			    tot += abs(tot-i);

			}
			tot += tab[i]-'0';

		}
		printf("Case #%d: %d\n",cnt++,inv );
	}
}