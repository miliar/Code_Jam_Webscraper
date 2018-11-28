#include <iostream>

using namespace std;

int case_i, case_n;

int main()
{	
	int k,c,s;
	cin >>  case_n;
	for (case_i = 1; case_i <= case_n; case_i++)
	{
		cout << "Case #" << case_i << ": ";
		cin >> k >> c >> s;
		if (c==1)
		{
			if (s < k)
			{
				cout << "IMPOSSIBLE\n";
				continue;
			}
			else
			{
				for (int i=1;i<k;i++)
					cout << i << ' ';
				cout << k << endl;
			}
		}
		else
		{
			if (s < k - 1)
			{
				cout << "IMPOSSIBLE\n";
				continue;
			}
			else
			{
				for (int i=2; i<k; i++)
					cout << i << ' ';
				cout << k << endl;
			}
		}
	}
	return 0;
}