#include <stdio.h>
#include <atlstr.h>

int GetLastNumber(int N)
{
	bool check[10] = {0, };
	CString strN;
	strN.Format(_T("%d"), N);

	for (int i=1; i<1000; i++)
	{
		CString strNumber;
		bool bSleep = true;

		strNumber.Format(_T("%d"), i*N);

		for (int j=0; j<=9; j++)
		{
			if (check[j]==false)
			{
				CString strDigit;
				strDigit.Format(_T("%d"), j);
				if (strNumber.FindOneOf(strDigit)!=-1)
				{
					check[j] = true;
				}
				else
				{
					bSleep = false;
				}
			}
		}

		if (bSleep)
			return N*i;

	}
	return -1;
}

int main()
{
	int T, N;
	FILE * in = fopen("A-large.in", "r");
	FILE * out = fopen("A-large.out", "w");

	fscanf(in, "%d", &T);

	for (int i=1; i<=T; i++)
	{
		int nResult;
		fscanf(in, "%d", &N);
		nResult = GetLastNumber(N);

		if (nResult < 0)
			fprintf(out, "Case #%d: INSOMNIA\n", i);
		else
			fprintf(out, "Case #%d: %d\n", i, nResult);
	}

	return 0;
}