#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, smax;
	string s;
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> smax >> s;
		int total = 0, need = 0;
		for(int j = 0; j <= smax; j++)
		{
			if(total < j)
			{
				need += (j - total);
				total = j;
			}
			total += ((int)(s[j] - '0'));
		}
		cout << "Case #" << i << ": " << need << endl;
	}
	return 0;
}