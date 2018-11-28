#include <stdio.h>
#include <set>

using namespace std;




int main()
{
	int T,c=1;
	scanf("%d",&T);

	while(T--)
	{
		set<int> firstcard[4];
		set<int> secondcard[4];
		int frow,srow;
		scanf("%d",&frow);

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				int value;
				scanf("%d",&value);
				firstcard[i].insert(value);
			}
		}
		scanf("%d",&srow);

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				int value;
				scanf("%d",&value);
				secondcard[i].insert(value);
			}
		}
		frow--;
		srow--;
		if(firstcard[frow] == secondcard[srow])
		{
			printf("Case #%d: Bad magician!\n",c++);
		}
		else
		{
			set<int> temp;
			set<int>::iterator sit;
			int size = 0;
			int answer = -1;
		
			for(sit=firstcard[frow].begin();sit!=firstcard[frow].end();sit++)
			{
				temp.insert(*sit);
				size++;
				if(answer==-1&&temp.size()!=size)
				{
					answer = *sit;
				}
			}
			for(sit=secondcard[srow].begin();sit!=secondcard[srow].end();sit++)
			{
				temp.insert(*sit);
				size++;
				if(answer==-1&&temp.size()!=size)
				{
					answer = *sit;
				}
			}
			if(answer == -1)
			{
				printf("Case #%d: Volunteer cheated!\n",c++);
			}
			else
			{
				if(size - temp.size() >=2)
				{
					printf("Case #%d: Bad magician!\n",c++);
				}
				else
				{
					printf("Case #%d: %d\n",c++,answer);
				}
			}
		}
	}
	return 0;
}