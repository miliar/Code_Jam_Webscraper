
#include<string>
#include<vector>
#include<stack>
#include<algorithm>
#include <map>
#include <queue>
#include <string.h>
#include <fstream>
#include <cmath>

using namespace std;

ofstream cout("out.txt");
ifstream cin("B-small-attempt0.in");

int main(void)
{

	int t;
	cin >> t;

	for (int tc = 1; tc <= t; tc++)
	{

		int a, b, k;
		cin >> a >> b >> k;

		int res = 0;
		for (int i = 0; i < a; i++)
		{
			for (int j = 0; j < b; j++)
			{
				if ( ((int)(i&j)) < k)
					res++;
			}
		}


		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}