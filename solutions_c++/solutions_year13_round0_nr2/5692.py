#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <tuple>

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

char pat[100][100];
char l[100][100];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		int lines, cols;

		printf("Case #%d: ",case_id);
		scanf("%d %d",&lines,&cols);
		
		for (int i = 0; i < lines; i++)
		{
			for (int j = 0; j < cols; j++)
			{
				scanf("%d", &pat[i][j]);
				l[i][j] = 100;
			}
		}


		//Lignes
		for (int i = 0; i < lines; i++)
		{
			int max = 0;
			for (int j = 0; j < cols; j++)
			{
				if (pat[i][j] > max)
				{
					max = pat[i][j];
				}
			}

			for (int j = 0; j < cols; j++)
			{
				if (l[i][j] > max)
				{
					l[i][j] = max;
				}
			}
		}

		//Colonnes
		for (int i = 0; i < cols; i++)
		{
			int max = 0;
			for (int j = 0; j < lines; j++)
			{
				if (pat[j][i] > max)
				{
					max = pat[j][i];
				}
			}

			for (int j = 0; j < lines; j++)
			{
				if (l[j][i] > max)
				{
					l[j][i] = max;
				}
			}
		}

		//Check
		bool okay = true;
		for (int i = 0; i < lines; i++)
		{
			for (int j = 0; j < cols; j++)
			{
				if (l[i][j] != pat[i][j])
				{
					okay = false;
					break;
				}
			}
			if (!okay)
			{
				break;
			}
		}

		if (okay)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
		
		fflush(stdout);
	}
	return 0;
}