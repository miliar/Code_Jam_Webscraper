#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int s1[4][4];
int s2[4][4];
int n, num1, num2;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d\n",&n);
	for (int i=0;i<n;i++)
	{
		scanf("%d", &num1);
		for (int ii = 0; ii<4; ii++)
			for (int j=0; j<4; j++)
				scanf("%d", &s1[ii][j]);
		scanf("%d", &num2);
		for (int ii = 0; ii<4; ii++)
			for (int j=0; j<4; j++)
				scanf("%d", &s2[ii][j]);
		int ans = -1;
		for (int j = 0; j<4; j++)
			for (int k=0; k<4; k++)
			{
				if (s1[num1-1][j] == s2[num2-1][k])
				{
					if (ans == -1) 
						ans = s1[num1-1][j];
					else
						ans = -2;
				}
			}
		
		if (ans == -1)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else if (ans == -2)
			printf("Case #%d: Bad magician!\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,ans);
	}
}
