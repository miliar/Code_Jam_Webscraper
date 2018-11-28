#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <climits>
#include <set>
using namespace std;
int fi[4][4];
int sec[4][4];
int ans1,ans2;
int main()
{
	// ios_base::sync_with_stdio(false);
	int t;
	scanf("%d",&t);
	for (int ca = 0; ca < t; ++ca)
	{
		cin>>ans1;
		ans1--;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				int num;
				cin>>num;
				fi[i][j]=num;
			}
		cin>>ans2;
		ans2--;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				int num;
				cin>>num;
				sec[i][j]=num;
			}
		vector<int> anss;
		for (int i = 0; i < 4; ++i)
			if(find(sec[ans2],&sec[ans2][4],fi[ans1][i])!=&sec[ans2][4])
				anss.push_back(fi[ans1][i]);
		if(anss.size()==1)
			printf("Case #%d: %d\n",ca+1,anss[0]);
		else if(anss.size()==0)
			printf("Case #%d: Volunteer cheated!\n",ca+1);
		else
			printf("Case #%d: Bad magician!\n",ca+1);
	}
	return 0;
}
