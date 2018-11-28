#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int T, t;
	cin >> T;
	t = 1;
	while (T >= t)
	{
		long long N, res;		
		cin >> N;
		int list[10] = {0 ,0, 0, 0, 0, 0, 0, 0, 0, 0 };

		res = 0;
		for (long long i = 1; i <= 2000; i++)
		{
			long long tmpNum = N*i;
			while (tmpNum > 0)
			{
				list[tmpNum % 10] = 1;
				tmpNum /= 10;
			}
			int j;
			for (j = 0; j < 10; j++)
			{
				if (list[j] == 0)
					break;
			}
			if (j == 10)
			{
				res = N*i;
				break;
			}
		}

		if( res == 0)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << t << ": " << res << endl;
		t++;
	}
}