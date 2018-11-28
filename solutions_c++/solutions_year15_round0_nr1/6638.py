#include <iostream>
using namespace std;

char A[1000] = { 0 };
int min = 10;
int cnt = 0;
int friends = 0;

void Initialize()
{
	min = 10;
	cnt = 0;
	friends = 0;

	for (int i = 0; i < 1000; i++)
		A[i] = 0;
}
int main()
{
	freopen("E:\\Dev\\A-small-attempt1.in", "r", stdin);
	FILE *fp = NULL;
	fp = fopen("E:\\output.in", "w");
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		Initialize();

		int sMax;
		cin >> sMax;
		cin >> A;

		for (int j = 0; j < sMax + 1; j++)
		{
			if (cnt >= j)
			{
				cnt += (A[j] - 48);
			}
			else
			{
				while (cnt < j)
				{
					friends++;
					cnt++;
				}
				cnt += (A[j]-48);
			}
		}

		cout << "Case #" << i + 1 << ": " << friends << endl;
		fprintf(fp, "Case #%d: %d\n", i + 1, friends);
	}
	fclose(fp);
}