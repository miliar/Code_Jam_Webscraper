#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		int num;
		cin >> num;
		string str;
		cin >> str;
		int sum = 0;
		int result = 0;
		for(int j=0; j<=num; j++)
		{
			if((sum + result) < j)
			{
				result += (j - sum - result);
			}
			sum += str[j] - '0';
		}

		cout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}