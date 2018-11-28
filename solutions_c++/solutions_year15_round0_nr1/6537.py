#include<iostream>
#include <vector>
#include <string>



using namespace std;



int main()
{



	int TOTAL;


	cin >> TOTAL;

	for (int test_iter = 1; test_iter <= TOTAL; test_iter++)
	
	{
		int xy[1000];
		int SMAXIMUM;
		string mystring;
		cin >> SMAXIMUM;
		cin >> mystring;
		int count = 0;
		int TEST = 0;



		for (int j = 0; j <= SMAXIMUM; j++)
		
		{
			if ((mystring[j] - '0')  && j > TEST) 
			
			{
				count += (j - TEST);
				TEST += (j - TEST);
			}

			TEST += (mystring[j] - '0');
		
		}

		xy[0] = 1;
		cout << "Case #" << test_iter << ": " << count << '\n';


	}
	return 0;
}