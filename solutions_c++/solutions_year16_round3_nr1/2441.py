
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define IN_FILE_NAME "A-large.in"
#define OUT_FILE_NAME "A-large.out"

bool sortp(const pair<int, int> &lhs, const pair<int, int> &rhs)
{
	return lhs.second > rhs.second;
}

int main()
{
	freopen(IN_FILE_NAME, "r", stdin);
	freopen(OUT_FILE_NAME, "w", stdout);

	int t, tests;
	scanf("%d", &tests);

	for(t=0; t<tests; t++)
	{
		int n;
		scanf("%d", &n);
		int total = 0;
		vector<pair<int,int>> arr;

		for(int i=0; i<n; i++)
		{
			int nr;
			scanf("%d", &nr);

			arr.push_back(pair<int,int>(i, nr));
			total += nr;
		}

		sort(arr.begin(), arr.end(), sortp);

		vector<pair<int,int>> order;

		/*if(n%2 == 1)
		{
			order.push_back(pair<int, int>(arr[0].first, -1));
			arr[0].second--;
			n--;
		}*/

		printf("Case #%d: ", t+1);
		for(int i=1; i<n; i++)
		{
			int diff = arr[0].second - arr[i].second;
			if(arr[0].second == arr[n-1].second)
				break;
			for(int k=0; k<diff; k++)
			{
				for(int j=0; j<i; j++)
				{
					printf("%c ", arr[j].first + 'A');
					arr[j].second--;
				}
			}
		}

		while(arr[0].second > 1)
		//for(int i=0; i<arr[0].second-1; i++)
		{
			printf("%c%c ", arr[0].first + 'A', arr[1].first +'A');
			arr[0].second--;
			arr[1].second--;
			for(int i=2; i<n; i++)
			{
				printf("%c ", arr[i].first + 'A');
				arr[i].second--;
			}
		}
		for(int i=0; i<n-2; i++)
		{
			printf("%c ", arr[i].first + 'A');
		}
		printf("%c%c\n", arr[n-2].first + 'A', arr[n-1].first + 'A');
	}
}