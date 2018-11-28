#include <iostream>
	using namespace std;
#include <cstdio>
#include <cstring>

char arr[4][4];
char chkWinner(void);
char secondchk(void);

int main(void)
{
	FILE *ifp, *ofp;

	int cnt;
	int prob = 1;
	char ms[20];
	char check = ' ';
	char secondCheck = ' ';
	
	ifp = fopen("input.in","rIN");
	ofp = fopen("output.txt","w");

	//cin >> cnt;
	fscanf(ifp,"%d",&cnt);

	for(int i=0 ; i<cnt ; ++i)
	{
		for(int j=0 ; j<4 ; ++j)
		{
			//scanf("%s", &arr[j]);
			fscanf(ifp,"%s",&arr[j]);
		}

		check = chkWinner();

		if(check == 'O')
		{
			strcpy(ms,"O won");
			//cout << "Case #" << prob++ << ": O Won" << endl;
			//fprintf(ofp,"Case #%d: O won\n", prob++);
		}
		else if(check == 'X')
		{
			strcpy(ms,"X won");
			//cout << "Case #" << prob++ << ": X Won" << endl;
			//fprintf(ofp,"Case #%d: X won\n", prob++);
		}
		else
		{
			secondCheck = secondchk();

			if(secondCheck == 'N')
			{
				strcpy(ms,"Game has not completed");
				//cout << "Case #" << prob++ << ": Game has not completed" << endl;
				//fprintf(ofp,"Case #%d: Game has not completed\n", prob++);
			}
			else if(secondCheck == 'D')
			{
				strcpy(ms,"Draw");
				//cout << "Case #" << prob++ << ": Draw" << endl;
				//fprintf(ofp,"Case #%d: Draw\n", prob++);
			}
		}

		fprintf(ofp,"Case #%d: %s\n",prob++,ms);
	}

	return 0;
}

char chkWinner(void)
{
	if(arr[0][0] == arr[1][1] && arr[1][1] == arr[2][2] && arr[2][2] == arr[3][3])
	{
		return arr[0][0];
	}
	else if(arr[0][0] == 'T' && arr[1][1] == arr[2][2] && arr[2][2] == arr[3][3])
	{
		return arr[1][1];
	}
	else if(arr[0][0] == arr[1][1] && arr[1][1] == arr[2][2] && arr[3][3] == 'T')
	{
		return arr[0][0];
	}

	if(arr[0][3] == arr[1][2] && arr[1][2] == arr[2][1] && arr[2][1] == arr[3][0])
	{
		return arr[0][3];
	}
	else if(arr[0][3] == 'T' && arr[1][2] == arr[2][1] && arr[2][1] == arr[3][0])
	{
		return arr[1][2];
	}
	else if(arr[0][3] == arr[1][2] && arr[1][2] == arr[2][1] && arr[3][0] == 'T')
	{
		return arr[0][3];
	}

	for(int i=0 ; i<4 ; ++i)
	{
		if(arr[i][0] == arr[i][1] && arr[i][0] == arr[i][2] && arr[i][0] == arr[i][3])
		{
			return arr[i][0];
		}
		else if(arr[i][0] == 'T' && arr[i][1] == arr[i][2] && arr[i][1] == arr[i][3])
		{
			return arr[i][1];
		}
		else if(arr[i][0] == arr[i][1] && arr[i][1] == arr[i][2] && arr[i][3] == 'T')
		{
			return arr[i][0];
		}
	}

	for(int i=0 ; i<4 ; ++i)
	{
		if(arr[0][i] == arr[1][i] && arr[0][i] == arr[2][i] && arr[0][i] == arr[3][i])
		{
			return arr[0][i];
		}
		else if(arr[0][i] == 'T' && arr[1][i] == arr[2][i] && arr[1][i] == arr[3][i])
		{
			return arr[1][i];
		}
		else if(arr[0][i] == arr[1][i] && arr[0][i] == arr[2][i] && arr[3][i] == 'T')
		{
			return arr[0][i];
		}
	}

	return ' ';
}

char secondchk(void)
{
	int sw;

	sw=0;

	for(int i=0 ; i<4 ; ++i)
	{
		for(int j=0 ; j<4 ; ++j)
		{
			if(arr[i][j] == '.')
			{
				sw = 1;
				break;
			}
		}
	}

	if(sw == 1)
	{
		return 'N';
	}
	else
	{
		return 'D';
	}
}