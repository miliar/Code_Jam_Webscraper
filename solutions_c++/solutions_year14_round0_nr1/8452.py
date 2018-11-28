#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int map1[4];
int map2[4];

int main()
{
    int t;
    scanf("%d", &t);
    int id = 1;
	while (t--)
	{
        int matches = 0;
        int matchedId = -1;
	
        int ans1;
		scanf("%d", &ans1);
		for (int i=1; i<=4; ++i)
		{
            if( i==ans1 )
            {
                scanf("%d %d %d %d", &map1[0], &map1[1], &map1[2], &map1[3]);
            }
            else
            {
                int null;
                scanf("%d %d %d %d", &null, &null, &null, &null);
            }
		}
		
		int ans2;
		scanf("%d", &ans2);
		for (int i=1; i<=4; ++i)
		{
            if( i==ans2 )
            {
                scanf("%d %d %d %d", &map2[0], &map2[1], &map2[2], &map2[3]);
                for (int j = 0; j < 4; ++j)
                {
                    for (int k = 0; k < 4; ++k)
                    {
                        if( map2[j]== map1[k] )
                        {
                            matchedId = j;
                            matches++;
                        }
                    }
                }
            }
            else
            {
                int null;
                scanf("%d %d %d %d", &null, &null, &null, &null);
            }
		}
		
		if( matches==0 )
            printf("Case #%d: Volunteer cheated!\n", id++);
		else if( matches==1 )
            printf("Case #%d: %d\n", id++, map2[matchedId]);
		else
            printf("Case #%d: Bad magician!\n", id++);
	}
	return 0;
}
