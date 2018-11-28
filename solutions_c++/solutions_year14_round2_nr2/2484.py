#include <iostream>
using namespace std;

int main()
{
	FILE *fp = fopen("input.txt", "r");
	int T, A, B, K;
	int count = 0;
	fscanf(fp, "%d", &T);
	int num = 1;
	while (T-- > 0)
	{
		fscanf(fp, "%d %d %d", &A, &B, &K);
		
		cout << "Case #" << num << ": ";
		count = 0;
		for (int i = 0; i < A; ++i)
		{
			for (int j = 0; j < B; ++j)
			{
				if ((i & j) < K)
				{
					++count;
				}
			}
		}
		cout << count << endl;

		++num;
	}
	fclose(fp);

	return 0;
}