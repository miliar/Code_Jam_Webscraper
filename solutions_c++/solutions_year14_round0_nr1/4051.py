#include <cstdio>
#include <cstring>
using namespace std;
int t, r, a;
int can[17];
void read()
{
	scanf("%d", &r);
	for (int j = 1; j <= 4; ++j)
		for (int k = 1; k <= 4; ++k)
		{
			scanf("%d", &a);
			if(r == j) can[a]++;
		}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		memset(can, 0, sizeof(int) * 17);
		read();
		read();
		int answer = -1;
		for (int j = 1; j <= 16; ++j)
		{
			if(answer != -1 && can[j] == 2) 
			{
				answer = 0;
				break;
			}
			if(answer == -1 && can[j] == 2) 
				answer = j;
		}
		printf("Case #%d: ", i);
		if(answer == -1) printf("Volunteer cheated!\n");
		else if(answer == 0) printf("Bad magician!\n");
		else printf("%d\n", answer);
	}
}