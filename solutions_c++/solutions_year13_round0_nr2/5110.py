#include <iostream>
#include <string>
#include <vector>
#include <map>
#define LAWN_MAX 100
#define LEVEL_MAX 100
using namespace std;

int lawn[LAWN_MAX][LAWN_MAX];
int num_rows, num_cols;
bool error = false;

bool markPath(int x, int y)
{
	bool markHorizontal = true, markVertical = true;
	for (int i = 0; i < num_cols; i++)
	{
		if (lawn[x][i] > abs(lawn[x][y]))
		{
			markHorizontal = false;
			break;
		}
	}
	for (int i = 0; i < num_rows; i++)
	{
		if (lawn[i][y] > abs(lawn[x][y]))
		{
			markVertical = false;
			break;
		}
	}
	if (markHorizontal)
	{
		for (int i = 0; i < num_cols; i++)
		{
			lawn[x][i] = lawn[x][i] > 0 ? lawn[x][i] * -1 : lawn[x][i];
		}
	}
	if (markVertical)
	{
		for (int i = 0; i < num_rows; i++)
		{
			lawn[i][y] = lawn[i][y] > 0 ? lawn[i][y] * -1 : lawn[i][y]; 
		}
	}

	return markHorizontal || markVertical;
}

bool getMin(int &x, int &y)
{
	int min = LEVEL_MAX;
	bool retval = false;
	for (int i = 0; i < num_rows; i++)
	{
		for (int j = 0; j < num_cols; j++)
		{
			if ((lawn[i][j] <= min) && (lawn[i][j] >= 0))
			{
				x = i;
				y = j;
				min = lawn[i][j];
				retval = true;
			}
		}
	}
	return retval;
}

void alg()
{
	cin >> num_rows;
	cin >> num_cols;
	for (int i = 0; i < num_rows; i++)
	{
		for (int j = 0; j < num_cols; j++)
		{
			cin >> lawn[i][j];
		}
	}

	int x,y;
	bool done = true;
	while(getMin(x, y))
	{
		if (!markPath(x, y))
		{
			done = false;
			break;
		}
	}
	if (!done)
	{
		cout << "NO" << endl;
	}
	else
	{
		cout << "YES" << endl;
	}
}

int main()
{
	int d;
	cin >> d;
	for (int case_no = 1; case_no <= d; ++case_no) {
		cout << "Case #" << case_no << ": ";
		alg();
	}
	return 0;
}
