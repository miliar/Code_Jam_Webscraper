#include<iostream>
using namespace std;
int A[4][4], B[4][4];
int judge(int tmp,int row)
{
	for (int i = 0; i < 4; i++)
	{
		if (tmp == B[row-1][i])
			return 1;
	}
	return 0;
}
int main()
{
	int T;
	
	errno_t err1; 
	FILE *f;
	err1 = freopen_s(&f, "A-small-attempt0.in", "r", stdin);
	errno_t err2;
	FILE *f2;
	err2 = freopen_s(&f2, "3.txt", "w", stdout);
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int a, b;
		cin >> a;
		for (int j = 0; j < 4;j++)
		for (int k = 0; k < 4; k++)
			cin >> A[j][k];
		cin >> b;
		for (int j = 0; j < 4; j++)
		for (int k = 0; k < 4; k++)
			cin >> B[j][k];
		int num = 0, t = 0;
		for (int j = 0; j < 4;j++)
		if (judge(A[a-1][j], b))
		{
			num ++;
			t = A[a-1][j];
		}
		if (num == 0)
			cout << "Case #" << i << ": Volunteer cheated!"<<endl;
		else
		{
			if (num == 1)
				cout << "Case #" << i << ": " << t << endl;
			else
				cout << "Case #" << i << ": Bad magician!" << endl;
		}
	}
	system("pause");
}