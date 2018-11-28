
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
#include <limits>
#include <cstring>

using namespace std;


int arr1[4][4],arr2[4][4];
int main()
{
	int T,c1,c2;
	scanf("%d",&T);
	for(int t = 1;t<=T;t++)
	{
		scanf("%d",&c1);
		for(int i = 0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&arr1[i][j]);

		scanf("%d",&c2);

		for(int i = 0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&arr2[i][j]);
		int count= 0,val;
		/*/for(int i = 0;i<4;i++)
			printf("arr1 = %d\n",arr1[c1-1][i] );

		for(int i = 0;i<4;i++)
			printf("arr2 = %d\n",arr2[c2-1][i] );*/
		for(int i = 0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{

				if(arr1[c1-1][i] == arr2[c2-1][j])
				{
					count++;
					// printf("i = %d j = %d\n",i,j);
					val = arr1[c1-1][i];
				}
			}
		}
		if(count == 0)
			printf("Case #%d: Volunteer cheated!\n",t);
		else if(count >1)
			printf("Case #%d: Bad magician!\n",t);
		else
			printf("Case #%d: %d\n",t,val);
	}	
	return 1;
}