//Kyle Hatfield
//ktbh4jc@gmail.com
//04/11/2015
//Omninos
#include <iostream>
using namespace std;
const int INIT_TO_ZERO = 0;
string winner = "hello";
int omnino_size, row, col, num_cases;

int main()
{
	cin >> num_cases;
	for (int i=INIT_TO_ZERO; i< num_cases; i++)
	{
		cin >> omnino_size >> row >> col;
		if ((row*col)%omnino_size != 0)
			winner = "RICHARD";
		else if(col < omnino_size && row < omnino_size)
			winner = "RICHARD";
		else if (omnino_size == 1 || omnino_size == 2)
			winner = "GABRIEL";
		else if( omnino_size < 7)
		{
			if(row >= omnino_size - 1 && col % omnino_size == 0)
				winner = "GABRIEL";
			else if (col >= omnino_size-1 && row % omnino_size == 0)
				winner = "GABRIEL";
			else
				winner = "RICHARD";
		}
		else
		{
			winner = "RICHARD";
		}
		cout << "Case #" << i+1 << ": " << winner << endl;
	}
	return INIT_TO_ZERO;
}