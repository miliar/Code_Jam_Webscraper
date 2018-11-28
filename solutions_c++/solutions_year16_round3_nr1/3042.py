#include "iostream"
using namespace std;
void senate(int A[], int n, char B[])
{
	bool yesr = true;
for(int i=0 ; i<n;i++)
{
	if (A[i]>0)
	{
		yesr = false;
		break;
	}
}
if (yesr)
{
	return;
}

	bool yes = false;
for(int i=0 ; i<n;i++)
{
	if (A[i]*(A[i]-1))
	{
		yes = true;
		break;
	}
}
if (yes)
{
	int max = A[0];
	int maxin =0;
	int maxin2 = -1;
	for (int i = 1; i < n; ++i)
	{
		if(A[i] == max)
		{
			maxin2 = i;
		}
		if(A[i] > max)
		{
			maxin2 = -1;
			maxin = i;
			max = A[i];
		}

	}
	if (maxin2 == -1)
	{
		A[maxin]--;
		cout << B[maxin] << " ";
		senate(A,n,B);
	}
	else
	{
		A[maxin]--;
		A[maxin2]--;
		cout << B[maxin]<<B[maxin2]<< " ";
		senate(A,n,B);
	}
}
else
{
	int sum = 0;
	for (int i = 0; i < n; ++i)
	{
		sum = sum + A[i];
	}
	int k = 0;
	while(sum >2)
	{
		if (A[k])
		{
			A[k]--;
			sum--;
			cout << B[k] << " ";
		}
		k++;
	}
	for (int i = 0; i < n; ++i)
	{
		if (A[i] > 0)
		{
			A[i]--;
			cout << B[i];
		}
	}

}
}
int main()
{
	char B[26];
	B[0] = 'A';
	B[1] = 'B';
	B[2] = 'C';
	B[3] = 'D';
	B[4] = 'E';
	B[5] = 'F';
	B[6] = 'G';
	B[7] = 'H';
	B[8] = 'I';
	B[9] = 'J';
	B[10] = 'K';
	B[11] = 'L';
	B[12] = 'M';
	B[13] = 'N';
	B[14] = 'O';
	B[15] = 'P';
	B[16] = 'Q';
	B[17] = 'R';
	B[18] = 'S';
	B[19] = 'T';
	B[20] = 'U';
	B[21] = 'V';
	B[22] = 'W';
	B[23] = 'X';
	B[24] = 'y';
	B[25] = 'Z';
int t;
int n;
cin >> t;
for (int i = 0; i < t; ++i)
{
	cin >> n;
	int A[n];
	for (int j = 0; j < n; ++j)
	{
		cin >> A[j];
	}
	cout << "Case #"<<(i+1)<<": ";
	senate(A,n,B);
	cout << endl;
}
}