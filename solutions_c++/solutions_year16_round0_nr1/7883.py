#include <bits/stdc++.h>

using namespace std;

int main()
{
	int testcases;

	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		unsigned long long int N;
		cin >> N;

		unsigned long long int temp = 0;

		bool digits[10] = {};

		int left = 10;
		int mult = 1;
		while(left && N)
		{
			temp = mult*N;
			while(temp)
			{
				int x = temp%10;
				if(digits[x] == false)
				{
					digits[x] = true;
					left--;
				}
				temp/=10;
			}

			if(left == 0)
				break;

			mult++;
		}

		if(N)
			cout << "Case #" << i + 1 << ": " << mult*N << endl;
		else
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
	}
}