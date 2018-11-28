#include <iostream>
#include <cstdio>
#include <set>
#include <string>


using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T, N;
	
	cin >> T;
	
	for (int i=0; i < T; i++)
	{

		cin >> N;
		int k = 1;
		set<char> digits;

		while (true)
		{
			string temp = to_string(k*N);
			
			for (int j = 0; j < temp.length();j++)
			{
				digits.insert(temp[j]);
			}

			if (N == 0)
			{
				cout << "Case #" << i+1 << ": INSOMNIA" << endl;
				break;
			}
			else if (digits.size() == 10)
			{
				cout << "Case #" << i+1 << ": " << k*N << endl;
				break;
			}
			
			k++;
		}

	}

	return 0;
}
