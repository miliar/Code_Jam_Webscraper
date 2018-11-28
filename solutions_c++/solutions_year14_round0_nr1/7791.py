#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int c=1; c<=T; c++)
	{
		int answer=-1;
		int volunteer, magician;
		int i,j,d1[4],d2[4],t;

		cin >> volunteer;
		for(i=1;i<=4;i++)
		{
			if(i==volunteer)
				for(j=0;j<4;j++)
					cin >> d1[j];
			else
				for(j=0;j<4;j++)
					cin >> t;
		}
		cin >> magician;
		for(i=1;i<=4;i++)
		{
			if(i==magician)
				for(j=0;j<4;j++)
					cin >> d2[j];
			else
				for(j=0;j<4;j++)
					cin >> t;
		}
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				if(d1[i]==d2[j])
				{
					if(answer==-1)
						answer=d1[i];
					else
						answer=0;
				}
			}

		if(answer == 0)
			printf("Case #%d: Bad magician!\n", c);
		else if(answer == -1)
			printf("Case #%d: Volunteer cheated!\n", c);			
		else
			printf("Case #%d: %d\n", c, answer);
	}
}