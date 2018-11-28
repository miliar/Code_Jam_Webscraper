#include <iostream>
using namespace std;

#define ABS(x) (((x) < 0) ? -1 * (x) : (x)) 


bool check_status (const int iteration, const int sum)
{
	if (3 == ABS (sum) || 4 == ABS (sum))
	{
		cout << "Case #" << iteration << ": " << ((sum < 0) ? "X" : "O") << " won" << endl;
		return true;
	}

	return false;
}


int main ()
{
  int cases;

  cin >> cases;

  for (int i = 0; i < cases; ++i)
  {
	int sum_row[4] = {0};
	int sum_col[4] = {0};
	int sum_main_diagonal = 0;
	int sum_secondary_diagonal = 0;

    for (int j = 0; j < 16; ++j)
    {
	  char x;
      cin >> x;

	  int equiv_num = 0;
	  switch (x)
	  {
	    case 'X' : equiv_num = -1;   break;
		case 'T' : equiv_num = 0;    break;
		case 'O' : equiv_num = 1;    break;
		case '.' : equiv_num = -100; break;
	  }

	  int row = j/4;
	  int col = j%4;

	  sum_row[row] += equiv_num;
	  sum_col[col] += equiv_num;

	  if (row == col)
	  {
		  sum_main_diagonal += equiv_num;
	  }
	  else if (3 == row+col)
	  {
		  sum_secondary_diagonal += equiv_num;
	  }
    }
 
    // Check for main diagonal
	if (check_status (i+1, sum_main_diagonal)) continue;
	if (check_status (i+1, sum_secondary_diagonal)) continue;

	int row_flag = false;
	// Check for rows
	for (int r = 0; r < 4; ++r)
	{
		if (check_status (i+1, sum_row[r]))
		{
			row_flag = true; break;
		}
	}

	if (row_flag) continue;

	int col_flag = false;
	// Check for cols
	for (int c = 0; c < 4; ++c)
	{
		if (check_status (i+1, sum_col[c]))
		{
			col_flag = true; break;
		}
	}

	if (col_flag) continue;

	bool draw_flag = false;
	// Either a draw or Game has not completed
	for (int r = 0; r < 4; ++r)
	{
		if (sum_row[r] < -4)
		{
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
			draw_flag = true; break;
		}
	}

	if (draw_flag) continue;
	
	cout << "Case #" << i+1 << ": Draw" << endl;
  }

  return 0;
}