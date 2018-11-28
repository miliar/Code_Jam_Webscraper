#include <iostream>

using namespace std;

int main()
{
		int t;
		unsigned int A[5][5];
		unsigned int B[5][5];
		unsigned int ans, ans1, ans2;
		unsigned short int noofans;
		int case1;


	case1 = 1;

	scanf ("%d", &t);

	while (t)
	{
		scanf ("%d", &ans1);

		for (int index1 = 1; index1<5; index1 ++)
			for (int index2 = 1; index2<5; index2 ++)
			{
				scanf ("%d", &A[index1][index2]);
			}
						
		scanf ("%d", &ans2);

		for (int index1 = 1; index1<5; index1 ++)
			for (int index2 = 1; index2<5; index2 ++)
			{
				scanf ("%d", &B[index1][index2]);
			}

		noofans = 0;

		for (int index1 = 1; index1<5; index1 ++)
			for (int index2 = 1; index2<5; index2 ++)
			{
				if (A[ans1][index1] == B[ans2][index2])
				{
					ans = A[ans1][index1];
					noofans++;
				}
			}
		
		
		
		printf ("Case #%d: ", case1);

		switch (noofans)
		{
		case 0:
			printf ("Volunteer cheated!\n");
			break;

		case 1:
			printf ("%d\n", ans);
			break;

		default:
			printf ("Bad magician!\n");
		}
	
		case1++;
		t--;
	}
}