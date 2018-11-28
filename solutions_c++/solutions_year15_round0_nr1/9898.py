#include <iostream>
using namespace std;

int main ()
{
	int T;
	int Case;
	int Smax;
	int Friends;
	int Aud;
	int SUM;
	cin >> T;
	for (Case =0 ; Case < T;Case++)
	{
		SUM = 0;
		Friends = 0;
		cin >> Smax >> Aud;
		int * Temp = new int[Smax+1];
		for (int i = Smax ; i >=0 ; i--)
		{
			Temp[i] = Aud%10;
			Aud /= 10;
		}
		for (int i = 0 ; i < Smax+1 ; i++)
		{
			if (SUM >= i)
			{
			SUM += Temp[i];
			}
			else
			{
				Friends += i - SUM;
				SUM = i + Temp[i];
			}
		}
		cout << "Case #"<<Case+1 <<": "<<Friends<<endl;
	}
	return 0;
}