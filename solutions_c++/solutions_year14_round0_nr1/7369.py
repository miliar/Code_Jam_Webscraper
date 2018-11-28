#include <Windows.h>
#include <stdio.h>
#include <iostream>

using namespace std;

void skip(int lines)
{
	for(int i = 1; i <= lines; i++)
	{
		int j = 0;
		scanf("%d %d %d %d\n",&j,&j,&j,&j);
	}
}
void solve()
{
	int max_cases = 0;
	cin >> max_cases;
	for(int icase = 0; icase < max_cases; icase++)
	{
		int row[4] = {0};

		int first_row = 0;
		cin >> first_row;
 		skip(first_row-1);
		scanf("%d %d %d %d\n", &row[0], &row[1], &row[2], &row[3]);

		skip(4-first_row);

		int second_row = 0;
		cin >> second_row;
		skip(second_row-1);

		int choise;
		int icount = 0;

		for(int j = 0; j < 4; j++)
		{
			int num = 0;
			cin >> num;
			for(int k = 0; k < 4; k++)
			{
				if(row[k] == num)
				{
					choise = num;
					icount++;
					break;
				}
			}
		}

		skip(4-second_row);

		if(icount > 1)
		{
			printf("Case #%d: Bad Magician!\n", icase+1);
		}
		else if( icount == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", icase+1);
		}
		else
		{
			printf("Case #%d: %d\n",icase+1, choise);
		}
	}
}
int main(int argc, char *argv[])
{
	bool bclose_stdin = false, bclose_stdout = false;
	if(argc > 1)
	{
			freopen(argv[1], "r", stdin);
			bclose_stdin = true;
	}
	if(argc > 2)
	{
			freopen(argv[2], "w", stdout);
			bclose_stdout = true;
	}

	solve();

	if(bclose_stdin)
	{
		fclose(stdin);
	}
	if(bclose_stdout)
	{
		fclose(stdout);
	}

	return 0;
}