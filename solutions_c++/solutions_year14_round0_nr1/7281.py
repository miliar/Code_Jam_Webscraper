#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <functional>
#include <queue>
using namespace std;

int main()
{
//	freopen("sample.txt", "r", stdin);
   
	int t;
	scanf("%d\n", &t);
	for(int i = 1; i <= t; i++)
	{
		vector<int> count(17, 0);
		int a1;
		scanf("%d", &a1);
		vector<vector<int> > da(4, vector<int>(4));
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &da[i][j]);
		for(int j = 0; j < 4; j++)
			count[da[a1 - 1][j]]++;
		int a2;
		scanf("%d", &a2);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &da[i][j]);
		for(int j = 0; j < 4; j++)
			count[da[a2 - 1][j]]++;

		int num = 0, val = 0;
		for(int i = 1; i < 17; i++)
			if(count[i] == 2)
				num++, val = i;

		printf("Case #%d: ", i);
		switch(num)
		{
			case 0:printf("Volunteer cheated!\n");break;
			case 1:printf("%d\n", val);break;
			default:printf("Bad magician!\n");break;
		}
	}

    return 0;
}