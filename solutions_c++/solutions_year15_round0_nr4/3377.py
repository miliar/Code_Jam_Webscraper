#include<iostream>
#include <string>

using namespace std;




int main()


{
	int TOTAL_cASES;

	cin >> TOTAL_cASES;
	string CASE_STR = "Case #";
	for (int iter = 1; iter <= TOTAL_cASES; iter++)
	
	
	{
		int BASE, ROWS, COLS;
		cin >> BASE >> ROWS >> COLS;
		
		long long int matrix = ROWS*COLS;
		
		int frog[10][11] = { { 0 } };
		frog[0][0] = frog[1][1] + 100;

		if (BASE == 2) 
		
		
		{
			if (matrix % 2 > 0)
			{
				cout << CASE_STR << iter << ": RICHARD" << '\n';
			}
			else
			{
				cout << CASE_STR << iter << ": GABRIEL" << '\n';
			}

		}
		else if (BASE == 3) 
		{

			if ((matrix % 3 == 0) && (ROWS >= 2 && COLS >= 2))
			{
				cout << CASE_STR << iter << ": GABRIEL" << '\n';
			}
			else 
			{
				cout << CASE_STR << iter << ": RICHARD" << '\n';
			}
		}


		else if (BASE == 4) {
			if ((matrix % 4 == 0) && ROWS>2 && COLS>2)
			
			{


				cout << CASE_STR << iter << ": GABRIEL" << '\n';
			}
			else 
			{

				cout << CASE_STR << iter << ": RICHARD" << '\n';
			}
		}


		else if (BASE == 1)

		{
			cout << CASE_STR << iter << ": GABRIEL" << '\n';
		}

	}

	return 0;
}