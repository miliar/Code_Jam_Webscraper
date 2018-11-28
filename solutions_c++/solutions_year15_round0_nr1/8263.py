#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	/*
	int Smax[T];
	string S[T];
	for (int i = 0; i < T; i ++)
	{
		cin >> Smax[i] >> S[i];
	}
	
	cout << T << endl;
	for (int i = 0; i < T; i ++)
	{
		cout << Smax[i] << " ";
		for (int j = 0; j <= Smax[i]; j ++)
			cout << S[i][j];
		cout << endl;
	}
	*/
	
	for (int i = 0; i < T; i ++)
	{
		int Smax;
		string S;
		cin >> Smax >> S;
		
		int ovations = 0, friends = 0;
		for (int j = 0; j <= Smax; j ++)
		{
			if ( (j > ovations) && (S[j] > 0) )
			{
				friends += j - ovations;
				ovations += j - ovations;
			}
			ovations += (int)S[j] - 48;
		}
		
		cout << "Case #" << i+1 << ": " << friends << endl;
	}
	
	return 0;
}
