#include <iostream>
#include <fstream>
#include <string>



using namespace std;

int main() 
{
	ifstream cin("A-small-attempt1.in");
	ofstream cout("A-small-attempt1.out");

	int t;
	int p;
	int num;
	int result;
	int sum;
	int invite;
	string str;

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		result = 0;
		sum = 0;
		cin >> p >> str;
		for (int j = 0; j <= p; j++)
		{
			invite = 0;
			num = str[j] - '0';
			if (sum < j) {
				invite = j - sum;
				result += invite;
			}
			sum += num + invite;

		}
		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}