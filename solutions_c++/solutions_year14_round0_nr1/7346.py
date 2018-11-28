#include<iostream>
using namespace std;
int main()
{
	int cs, csi;
	csi ^= csi;
	cin >> cs;
	while (csi++ < cs)
	{
		int ha, hb;
		int A[4], B[4];
		cin >> ha;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (ha != (i + 1)) cin >> hb;
				else cin >> A[j];
			}
		}
		cin >> hb;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (hb != (i + 1)) cin >> ha;
				else cin >> B[j];
			}
		}
		hb = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (A[i] == B[j])
				{
					ha = A[i];
					hb++;
				}
			}
		}
		cout << "Case #" << csi << ": ";
		if (hb == 0) cout << "Volunteer cheated!";
		if (hb == 1) cout << ha;
		if (hb >= 2) cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}