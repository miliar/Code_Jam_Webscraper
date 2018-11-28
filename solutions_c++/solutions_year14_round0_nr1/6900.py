#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 0; t < T; t++)
	{
		int A;
		cin >> A;

		int* a = new int[16];
		for(int i = 0; i < 16; i++)
			cin >> a[i];

		int B;
		int* b = new int[16];
		cin >> B;

		for(int i = 0; i < 16; i++)
			cin >> b[i];


		int match = 0;
		int card = 0;
		for(int i = (A-1)*4; i < (A-1)*4+4; i++)
		{
			for(int j = (B-1)*4; j < (B-1)*4+4; j++)
			{
				if(a[i] == b[j])
				{
					match++;
					card = a[i];
				}
			}	
		}

		cout << "Case #" << (t+1) << ": ";
		if(match == 1)
			cout << card << endl;
		else if(match > 1)
			cout << "Bad magician!" << endl;
		else if(match == 0)
			cout << "Volunteer cheated!" << endl;
	}
}
