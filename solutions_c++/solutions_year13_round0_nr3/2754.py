#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

string str(int i) 
{
	char s[100];
	sprintf(s, "%d", i);
	return string(s); 
}

bool isPal(string str)
{
	for(int i = 0; i < str.size()/2; ++i)
		if(str[i] != str[str.size()-i-1])
			return false;
	return true;
}

int main()
{
	int cases;
	cin >> cases;
	for(int cs = 0; cs < cases; ++cs)
	{
		int a, b;
		cin >> a >> b;

		int sqrA = int(sqrt((double)a));
		if(sqrA*sqrA < a) ++sqrA;

		int sqrB = int(sqrt((double)b));

		int sum = 0;
		for(int i = sqrA; i <= sqrB; ++i)
		{
			int sqr = i*i;
			if(isPal(str(i)) && isPal(str(sqr)))
				++sum;
		}

		cout << "Case #" << cs+1 << ": " << sum << endl;
	}
	return 0;
}
