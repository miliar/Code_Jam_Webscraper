#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
using namespace std;

int before[ 4 ];
int after[ 4 ];

#define FILEIN

int main()
{
	int T;
	int br, ar, t;

	fstream in("test.in");
	fstream out("res.out");
	in>>T;

//	scanf("%d", &T);


	for (int i = 1; i <= T; i ++)
	{

		in>>br;

//		scanf("%d", &br);


		for (int j = 1; j <= 4; j ++)
		{
			for (int k = 1; k <= 4; k ++)
			{

				in>>t;

//				scanf("%d", &t);

				if (j == br)
				{
					before[ k - 1 ] = t;
				}
			}
		}


		in>>ar;

//		scanf("%d", &ar);

		for (int j = 1; j <= 4; j ++)
		{
			for (int k = 1; k <= 4; k ++)
			{

				in>>t;

//				scanf("%d", &t);

				if (j == ar)
				{
					after[ k - 1 ] = t;
				}
			}
		}

		int cnt = 0;
//		sort(before, before + 4);
//		sort(after, after + 4);
		for (int j = 0; j < 4; j ++)
		{
			for (int k = 0; k < 4; k ++)
			{
				if (before[ j ] == after[ k ])
				{
					cnt ++;
					t = before[ j ];
					break;
				}
			}
		}
		if (cnt == 0)
		{
			out<<"Case #"<<i<<": Volunteer cheated!"<<endl;

//			printf("Case #%d: Volunteer cheated!\n", i);

		}
		else if(cnt == 1)
		{

			out<<"Case #"<<i<<": "<<t<<endl;

//			printf("Case #%d: %d\n", i, t);

		}
		else
		{

			out<<"Case #"<<i<<": Bad magician!"<<endl;

//			printf("Case #%d: Bad magician!\n", i);
//
		}
	}
	return 0;
}