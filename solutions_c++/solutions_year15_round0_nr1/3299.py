#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int ncase;
	
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	cin >> ncase;

	for(int icase = 0;icase < ncase;icase++)
	{
		int n;
		string shyPerson;
		cin >> n;
		cin >> shyPerson;

		int res = 0;
		int standNum = 0;
		
		for(int i = 0;i <= n;i++)
		{
			if (standNum < i)
			{
				res += i - standNum;
				standNum = i;
			}
			standNum += shyPerson[i] - '0';
		}

		cout << "Case #" << icase + 1 << ": " << res << endl;
	}

	return 0;
}
