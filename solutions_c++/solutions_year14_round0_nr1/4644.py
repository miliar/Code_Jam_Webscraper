#include <iostream>;
#include <stdio.h>
#include <string>


using namespace std;

int main()
{
	int T,A,B;
	int list[4];
	int num;
	string s;
	int count = 0;
	int value = 0;
	scanf("%d", &T);
	for(int index = 1; index <= T; index++)
	{
		count = 0;
		value = 0;

		scanf("%d", &A);


		int AA = 4 - A;
		A--;
		getchar();
		while(A--)	
			getline(cin, s);
		for(int i = 0; i < 4; i++)
			scanf("%d", &list[i]);
		getchar();
		while(AA--) getline(cin, s);

		scanf("%d", &B);
		int BB = 4 - B;
		B--;
		getchar();
		while(B--) 
			getline(cin, s);
		for(int i = 0; i < 4; i++)
		{
			scanf("%d", &num);
			for(int j = 0; j < 4; j++)
			{
				if(list[j] == num)
				{
					count++;
					value = num;
				}
			}
		}
		getchar();
		while(BB--) getline(cin, s);

		if(count == 1)
			printf("Case #%d: %d\n", index, value);
		else if(count == 0)
			printf("Case #%d: Volunteer cheated!\n", index);
		else
			printf("Case #%d: Bad magician!\n", index);

	}


	//system("pause");
	return 0;
}

