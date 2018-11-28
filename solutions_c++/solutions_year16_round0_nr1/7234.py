#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

__int64 n;
int main()
{
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		__int64 nn;
		cin >> nn;

		__int64 j = 1;
		__int64 ln = 0;
		bool asd[10] = { false, false, false, false, false, false, false, false, false, false };
		while (true) 
		{
			__int64 cn = 0;
			__int64 kn = j * nn;
			while (kn > 0)
			{
				__int64 nnn = kn % 10;
				if (!asd[nnn])
				{
					asd[nnn] = true;
					cn++;
				}	
				kn /= 10;
			}

			ln += cn;
			if (j > 1000000000 || ln == 10)
				break;

			++j;
		}

		if (ln == 10) 
			printf("Case #%d: %lld\n", i + 1, j*nn);
		else
			printf("Case #%d: INSOMNIA\n", i + 1);
	}
}