
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64_t;


int  card1[4];
int  card2[4];
int  list[16];

int main()
{
    fgets(buf, 1024, stdin);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int ans1, ans2;
		fgets(buf, 1024, stdin);
		ans1 = atoi(buf);

		for(int j=0; j<4; j++)
		{
            fgets(buf, 255, stdin);
			if (j+1 == ans1)
				sscanf(buf, "%d %d %d %d", &card1[0], &card1[1], &card1[2], &card1[3]);
		}
		fgets(buf, 1024, stdin);
		ans2 = atoi(buf);

		for(int j=0; j<4; j++)
		{
			fgets(buf, 255, stdin);
			if (j+1 == ans2)
				sscanf(buf, "%d %d %d %d", &card2[0], &card2[1], &card2[2], &card2[3]);
		}

// 		for(int j=0; j<4; j++)
// 			printf("%d\n", card1[j]);
// 		for(int j=0; j<4; j++)
// 			printf("%d\n", card2[j]);

		for(int j=0; j<16; j++)
			list[j] = 0;
		for(int j=0; j<4; j++)
			list[card1[j]-1] = 1;
		int found_at = 0;
		int sum = 0;
		for(int j=0; j<4; j++)
		{
			sum += list[card2[j]-1];
			if (list[card2[j]-1] == 1)
				found_at = card2[j];
		}

		const char *res = "";
		if (sum == 1)
			printf("Case #%d: %d", i, found_at);
		else if (sum == 0)
			printf("Case #%d: Volunteer cheated!", i);
		else
			printf("Case #%d: Bad magician!", i);
		
		printf("\n");
	}
  
	return  0;  
}
