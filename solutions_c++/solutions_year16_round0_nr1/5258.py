#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

int main()
{
	int T = 0;

	cin >> T;

	for (long long i = 1; i <= T; i++ )
	{
		long long N = 0;
		vector <int> v;
		v.resize(10, 0);

		cin >> N;
		if(N == 0) cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		else
		{
			long long j = 1;
			bool multiply = true;
			bool x = true;
			while(multiply && x)
			{
				long long temp = j * N;
				while(temp != 0)
				{
					v[temp % 10]++;
					temp = temp / 10;
				}
				for(int k = 0; k < 10; k++)
				{
					if(v[k] == 0)
					{
						break;
					}
					if(k == 9) x = false;
				}
				if(x) j++;
			}
			cout << "Case #" << i << ": "<< N * j << endl;
		}

	}

	return 0;
}


