#include <iostream>
using namespace std;

char Data[10000];

#define NUM 1
#define I 2
#define J 3
#define K 4

int Table[5][5] = { { 0, 0, 0, 0, 0 },
					{ 0, NUM, I, J, K },
					{ 0, I, -NUM, K, -J },
					{ 0, J, -K, -NUM, I },
					{ 0, K, J, -I, -NUM } };

void Init(int len)
{
	for (int i = 0; i < len; i++)
	{
		if (Data[i] == 'i')
			Data[i] = I;
		if (Data[i] == 'j')
			Data[i] = J;
		if (Data[i] == 'k')
			Data[i] = K;
	}
}


int Calculate(int L, int X)
{
	int current = 0;
	int prevPos1 = -1;
	int prevPos2 = -1;

	int prevVal1 = 0;
	int prevVal2 = 0;

	int cont = 0;

	for (int j = 0; j < X; j++)
	{
		for (int k = 0; k < L; k++)
		{
			if (j == 0 && k == 0)
				current = 1;

			if (current > 0)
				current = Table[current][Data[k]];
			else if (current < 0)
				current = Table[-current][Data[k]] * (-1);
			else
				current = Data[k];

			if (prevPos1 == -1)
			{
				if (current == I || current == -I)
				{
					prevPos1 = k + (j * L);
					prevVal1 = current;
					current = 0;
					continue;
				}
			}
			else if (prevPos2 == -1)
			{
				if (current == J || current == -J)
				{
					prevPos2 = k + (j * L);
					prevVal2 = current;
					current = 0;
					continue;
				}
			}
		}
	}

	int result = 0;
	if (current == K || current == -K)
	{
		result = prevVal1 * prevVal2 * current;
	}

	if (result == 24)
		return 1;
	return 0;
}

int main()
{
	freopen("E:\\Dev\\C-small-attempt0.in", "r", stdin);
	
	FILE *fp = NULL;
	fp = fopen("E:\\output.out", "w");
	
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int L;
		int X;
		cin >> L;
		cin >> X;
		cin >> Data;
		Init(L);

		int result = Calculate(L, X);
		if (result == 1)
		{
			cout << "Case #" << i + 1 << ": " << "YES" << endl;
			fprintf(fp, "Case #%d: YES\n", i + 1);
		}
		else
		{
			cout << "Case #" << i + 1 << ": " << "NO" << endl;
			fprintf(fp, "Case #%d: NO\n", i + 1);
		}
		
		
	}
	fclose(fp);
}