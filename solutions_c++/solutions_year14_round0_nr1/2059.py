#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <fstream>

using namespace std;

int main()
{

	freopen("input.txt","r",stdin);

	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++)
	{
		int a1;
		scanf("%d",&a1);
		vector<int> possibleAns;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				int x;
				scanf("%d",&x);
				if( i == a1-1 )
					possibleAns.push_back(x);
			}
		int a2;
		scanf("%d",&a2);
		vector<int> trueAns;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				int x;
				scanf("%d",&x);
				if( i == a2-1 )
					trueAns.push_back(x);
			}
		int intersection = 0;
		int val = -1;
		for(int i=0;i<possibleAns.size();i++)
			for(int j=0;j<trueAns.size();j++)
				if( possibleAns[i] == trueAns[j] )
				{
					intersection++;
					val = possibleAns[i];
				}
		printf("Case #%d: ",t);
		if( intersection == 0 )
		{
			printf("Volunteer cheated!\n");
		}
		else if( intersection == 1 )
		{
			printf("%d\n",val);
		}
		else
		{
			printf("Bad magician!\n");
		}
	}

	return 0;

}
