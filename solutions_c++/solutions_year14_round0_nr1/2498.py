// #include "include\preCompile\KL_PreCompile.hpp"

#include "KL_PreCompile.hpp"

// < input.in > output.out
void init()
{
}

int main()
{
	clock_t time1;
	time1 = clock();

	freopen("D:\\DUMP\\input.in", "r", stdin);
	freopen("D:\\DUMP\\output.out", "w", stdout);

	int T;
	cin >> T;

	int arr[4][4][2] = {0};
	int userAns[2] = {0};
	for (long long int caseNum = 1; caseNum <= T; caseNum++)
	{

		KL_FOR_DEF(round, 2)
		{
			cin >> userAns[round];

			KL_FOR_DEF(i, 4)
			{
				KL_FOR_DEF(j, 4)
				{
					cin >> arr[i][j][round];
				}
			}
		}

		int count = 0;
		int index = -1;
		//int row = -1;
		//int col = -1;

		int val = -1;
		KL_FOR_DEF(i, 4)
		{
			KL_FOR_DEF(j, 4)
			{
				int f = arr[userAns[0]-1][i][0];
				int l = arr[userAns[1]-1][j][1];

				if ( f == l )
				{
					count++;	
					val = f;
					//row = userAns[0]-1;
					//col = i;
				}
			}
		}

		cout << "Case #" << caseNum << ": ";

		if (0 == count)
		{
			cout << "Volunteer cheated!";
		}
		else if (1 == count)
		{
			cout << val;
		}
		else if (1 < count)
		{
			cout << "Bad magician!";
		}

		cout << endl;
		//if (userAns[0] == userAns[1])
		//{
		//	cout << "Bad magician!" << endl;
		//}

	}

#if 0
	clock_t time2, timeTaken;
	time2 = clock();
	timeTaken = time2 - time1;
	long long int seconds = timeTaken/CLOCKS_PER_SEC;
	long long int minutes = seconds/60;
	seconds %= 60;
	cout << minutes << "min" << seconds << "sec";
#endif



	fclose(stdin);
	fclose(stdout);
}
