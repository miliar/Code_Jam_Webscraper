#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    int task;
    scanf("%d", &task);
    for (int t = 1; t <= task; ++t)
    {
	int answer1, square1[5][5], square2[5][5];
	int answer2, haveNo[20];
	scanf("%d", &answer1);
	for (int i = 1; i <= 4; ++i)
	    for (int j = 1; j <= 4; ++j)
		scanf("%d", &square1[i][j]);
	scanf("%d", &answer2);
	for (int i = 1; i <= 4; ++i)
	    for (int j = 1; j <= 4; ++j)
		scanf("%d", &square2[i][j]);
	memset(haveNo, 0, sizeof(haveNo));
	for (int i = 1; i <= 4; ++i)
	{
	    haveNo[square1[answer1][i]]++;
	    haveNo[square2[answer2][i]]++;
	}
	int num = 0, flag;
	for (int i = 1; i <= 16; ++i)
	    if (haveNo[i] >= 2) ++num, flag = i;
	printf("Case #%d: ", t);
	if (num == 1)
	    printf("%d\n", flag);
	else if(num == 0) 
	    printf("Volunteer cheated!\n");
	else printf("Bad magician!\n");
    }
    return 0;
}
