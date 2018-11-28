#include<iostream>
using namespace std;
double A[1000] = {0};
double B[1000] = {0};
double C[1000] = {0};
double D[1000] = {0};
int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n;
		int n1 = 0, n2 = 0;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> A[j];
			C[j] = A[j];
		}
		for (int j = 0; j < n; j++)
		{
			cin >> B[j];
			D[j] = B[j];
		}
		for (int j = 0; j < n; j++)
		{
			double temp = 2;
			double M = 2;
			int flag1 = -1;
			int flag = -1;
			for (int k = 0; k < n; k++)
			{
				if (B[k] > A[j] && B[k] < temp)
				{
					temp = B[k];
					flag = k;
				}
				if (B[k] < M && B[k] != 0)
				{
					M = B[k];
					flag1 = k;
				}
			}
			if (flag != -1)
			{
				B[flag] = 0;
				A[j] = 0;
			}
			else
			{
				B[flag1] = 0;
				A[j] = 0;
				n2++;
			}
		}
		for (int j = 0; j < n; j++)
                {
                        double temp = 2;
                        double M = 2;
                        int flag1 = -1;
                        int flag = -1;
                        for (int k = 0; k < n; k++)
                        {
                                if (C[k] > D[j] && C[k] < temp)
                                {
                                        temp = C[k];
                                        flag = k;
                                }
                                if (C[k] < M && C[k] != 0)
                                {
                                        M = C[k];
                                        flag1 = k;
                                }
                        }
                        if (flag != -1)
                        {
                                C[flag] = 0;
                                D[j] = 0;
                                n1++;
                        }
                        else
                        {
                                C[flag1] = 0;
                                D[j] = 0;
                        }
                }
		cout << "Case #" << i + 1 << ": " << n1 << " " << n2 << endl;
	}
	return 0;
}
		
