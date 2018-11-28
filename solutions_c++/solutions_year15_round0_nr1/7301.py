///////////////////////////////////////////////////
// File name: A-large-0.cpp
// Author: Layton Wang
// Email Address: wangzixu.china@gmail.com
// Description: Google Code Jam 2015 Qualification Round Question 1
// Last Edited: 11 Apr 2015
///////////////////////////////////////////////////

#include <iostream>

int main( void )
{
	using std::cin;
	using std::cout;
	using std::endl;
	using std::string;

	unsigned case_num;
	cin >> case_num;

	for (unsigned i = 0; i < case_num; ++i)
	{
		/* code */
		unsigned Smax = 0;
		cin >> Smax;
		string audience;
		cin >> audience;
		unsigned sum = 0;
		unsigned friends_needed = 0;
		sum = audience[0] - 48;
		for (unsigned j = 1; j <= Smax; ++j)
		{
			while (sum < j && audience[j] - 48 != 0)
			{
				++friends_needed;
				++sum;
			}
			sum += audience[j] - 48;
		}
		cout << "Case #" << i + 1 << ": " << friends_needed << endl;
	}
	
	return 0;
}
