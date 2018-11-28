#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <utility>
#include <map>

using namespace std;

char buffer[2048];

#define FILE_NAME "B-small-attempt0"
#define ULL unsigned long long
#define CASET1 int _t=0, case_num;scanf("%d", &case_num);while(++_t<=case_num)
#define CASET2 int _t=0, case_num;gets(buffer);case_num=atoi(buffer);while(++_t<=case_num)

typedef vector<int> VI;
typedef vector<VI> VVI;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char dir[4] = {'E', 'S', 'W', 'N'};

int arr[1024][1024];
int SIZE;
int flag[1024];

VI src, dst;
int s, d, t;


int main()
{
	sprintf(buffer, "%s.in", FILE_NAME);
	freopen(buffer, "r", stdin);
	sprintf(buffer, "%s.out", FILE_NAME);
	freopen(buffer, "w", stdout);

	CASET1
	{
		printf("Case #%d: ", _t);
	
		scanf("%d%d%d", &s, &d, &t);
		
		int counter = 0;
		for(int i=0;i<s;i++)
		{
			for(int j=0;j<d;j++)
				if((i&j)<t)
					counter++;
		}

		printf("%d", counter);

		printf("\n");
	}
		
	return 0;
}