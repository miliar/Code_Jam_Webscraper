#include <iostream>
#include <stdio.h>
#include <sstream>
#include <math.h>

using namespace std;

int A;
int B;

bool isFair(const string& str)
{
	int length = str.length();
	for(int i = 0; i < length - i; ++i )
	{
		if(str[i] != str[length - i - 1])
		{
			//cout << str << endl;
			return false;
		}
	}
	//cout << str << " true" << endl;
	return true;
}

string getString(unsigned long long int v)
{
	string number;
	stringstream ss;
	ss << v;
	ss >> number;
	return number;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i)
	{
		int result = 0;
		cin >> A; cin >> B;
		unsigned long long int l = (unsigned long long int)sqrt(A);
		for(unsigned long long int j = l; j * j <= B; ++j)
		{
			if( j * j < A )
			{
				continue;
			}
			if( isFair( getString(j) ) && isFair( getString( j * j ) ) )
			{
				++result;
			}
		}
		printf("Case #%d: %d", i+1, result);
		cout << endl;
	}

	return 0;
}

