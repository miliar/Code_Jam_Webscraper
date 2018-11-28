#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin >> T;

	vector<int> cnt;

	for(int t = 1; t <= T; ++t)
	{
		cnt.assign(16, 0);

		int pick;

		for(int c = 0; c < 2; ++c)
		{
			cin >> pick;
			for(int i = 1; i <= 4; ++i)
				for(int j = 1; j <= 4; ++j)
				{
					int a;
					cin >> a;
					--a;
					if(i == pick)
						cnt[a]++;
				}
		}

		int r = -1;

		for(int i = 0; i < 16; ++i)
			if(cnt[i] == 2)
			{
				if(r == -1)
					r = i;
				else
					r = -2;
			}

		cout << "Case #" << t << ": ";
		if(r == -1)
			cout << "Volunteer cheated!" << endl;
		else if(r == -2)
			cout << "Bad magician!" << endl;
		else
			cout << r+1 << endl;
	}
}
