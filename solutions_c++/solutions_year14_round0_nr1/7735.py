#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	int T, t=0, r[4], index, b[4][4];
	cin >> T;
	int m[T][4];
	for (int i=0; i<T; i++)
	{
		int a;
	cin >> a;
	for (int j=0; j<4; j++)
		for (int k=0; k<4; k++)
			{	
				int num;
				cin>>num;
				if(j == a-1)
					m[i][k] = num;
			}
	cin >> a;		
	for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{	int num;
					cin >> num;
				if (j==a-1)
				{
					for (int p=0; p < 4; p++)
					{
						if (m[i][p] == num)
							{
								index = num;
								t++;
								break;
							}
					}
				}
			}			
		}
		if (t>1)
				cout << "Case #" << i+1 << ": Bad magician!" << '\n';
		else
		if (t==1)
				cout << "Case #" << i+1 << ": " <<index << '\n';
		else
		if (t==0)
				cout << "Case #" << i+1 << ": Volunteer cheated!" << '\n';
			t=0;
	//		r[4]=0;
	}
	return 0;
}
