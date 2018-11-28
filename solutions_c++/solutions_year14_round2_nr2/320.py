#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[])
{
	freopen("C:\\codejam\\B-large (1).in","r",stdin);
    freopen("C:\\codejam\\bL.out","w",stdout);
	long long int T, A, B, K;
	long long int count = 0;
	scanf("%d", &T);
	long long int num = 1;
	while (T-- > 0)
	{
		//printf("%lld\n", T);
		//fflush(fp1);
		scanf("%lld %lld %lld", &A, &B, &K);

		cout << "Case #" << num << ": ";
		count = 0;
		if (A <= K || B <= K)
		{
			count = A * B;
		}
		else
		{
			//cout << A << " " << B << " " << K << endl;
			count += A * K;
			count += B * K;
			count -= K * K;
			//cout << count << endl;
			long long int temp = 0;

			int min, max;
			if (A < B)
			{
				min = A;
				max = B;
			}
			else
			{
				min = B;
				max = A;
			}

			for (int i = K; i < min; ++i)
			{
				for (int j = i + 1; j < min; ++j)
				{
					if ((i & j) < K)
					{
						++temp;
					}
				}
			}

			count += 2 * temp;

			for (int i = min; i < max; ++i)
			{
				for (int j = K; j < min; ++j)
				{
					if ((i & j) < K)
					{
						++count;
					}
				}
			}
		}
		cout << count << endl;

		++num;
	}
	//fclose(fp);
	//fclose(fp1);

	return 0;
}
