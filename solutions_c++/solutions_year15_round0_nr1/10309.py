//============================================================================
// Name        : StandingOvation.cpp
// Author      : Ricky
//============================================================================
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int main() {

	std::fstream fs;
	fs.open ("Input.txt", std::fstream::in);

	std::string strInput;
	getline(fs, strInput);

	int T = atoi(strInput.c_str()); // Number of test cases
	for(int i=0;i<T;i++)
	{
		int tc_len;
		fs >> tc_len;

		int arr[tc_len+1];

		for(int j=0;j<tc_len+1;j++)
		{
			char temp;
			fs >> temp;
			arr[j] = temp - '0';
//			cout << arr[j];
		}
//		cout << endl;

		int result = arr[0];
//		cout << result << endl;
		int out = 0;

		for(int k=1;k<tc_len+1;k++)
		{
			if(k <= result)
			{
				result = result + arr[k];
			}
			else if (k > result)
			{
				if(arr[k] != 0)
				{
					out = k - result;
					result = result + arr[k];
				}
			}
		}

		cout << "Case #" << i+1 << ":" << " " << out << endl;
	}

	return 0;
}

