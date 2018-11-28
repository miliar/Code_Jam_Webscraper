#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <regex>

using namespace std;

void binary(int number) {
	int remainder;

	if(number <= 1) {
		cout << number;
		return;
	}

	remainder = number%2;
	binary(number >> 1);    
	cout << remainder;
}

void createBinary(string& s, int A)
{
	for (int c = 8; c >= 0; c--)
	{
		    int k = A >> c;
		    if (k & 1)
		      s.push_back('1');
		    else
		      s.push_back('0');
	}
}

int main(void)
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		int A,B,K;

		cin >> A >> B >> K;

		int count = 0;
		for (int i = 0; i < A; ++i)
		{
			for (int j = 0; j < B; ++j)
			{
				int val = i & j;
				if (val < K)
				{
					count++;
					// cout << "for (i,j) - " << i << "," << j << " " << val << endl;
				}
				
			}
		}

		cout << "case #" << t+1 << ": " << count << endl;
		// cout << endl << "count" << count << endl;
	}
	cout << endl;
	return 0;
}