#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

int main()
{
	int tests;
	cin >> tests;

	for(int a=0; a<tests; a++)
	{
		int x, rows, cols;
		cin >> x >> rows >> cols;

		string answer = "RICHARD";

		if(x == 1)
		{
			answer = "GABRIEL";
		}
		else if(x == 2)
		{
			int area = rows * cols;
			if((area % 2) != 0)
			{
				answer = "RICHARD";
			}
			else
			{
				answer = "GABRIEL";
			}
		}
		else if(x == 3)
		{
			int area = rows * cols;
			if((area % x) != 0)
			{
				answer = "RICHARD";
			}
			else if((area == x) || ((x < rows) && (x < cols)))
			{
				answer = "RICHARD";
			}
			else
			{
				answer = "GABRIEL";
			}
		}
		else if(x == 4)
		{
			int area = rows * cols;
			if((area % x) != 0)
			{
				answer = "RICHARD";
			}
			else if((area == x) || ((x < rows) && (x < cols)))
			{
				answer = "RICHARD";
			}
			else if(((rows == 2) && (cols == 4)) || ((rows == 4) && (cols == 2)))
			{
				answer = "RICHARD";
			}
			else if(((rows == 1) && (cols == 4)) || ((rows == 4) && (cols == 1)))
			{
				answer = "RICHARD";
			}
			else
			{
				answer = "GABRIEL";
			}
		}


		cout << "Case #" << (a+1) << ": " << answer << endl;
	}

	return 0;
}