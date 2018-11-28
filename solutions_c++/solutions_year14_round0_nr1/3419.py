#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	int f,s;
	int A[4][4],B[4][4];
	for (int i = 1 ; i <=T; i++)
	{
		cin >> f;
		for (int k = 0; k < 4; k++)
			for (int j = 0; j < 4; j++)
				cin >> A[k][j];
		cin >> s;
		for (int k = 0; k < 4; k++)
			for (int j = 0; j < 4; j++)
				cin >> B[k][j];
		int right = 0,value;
		for (int l = 0; l < 4; l++)
		{
			for (int m = 0; m < 4;m++)
			{
				if (A[f-1][l] == B[s-1][m])
				{	
					right++;
					value = A[f-1][l];
				}	
			}
		
		}
		if (right == 1)
			cout << "Case #"<<i<<": "<<value<<endl;
		else if (right > 1)
			cout << "Case #"<<i<<": "<<"Bad magician!"<<endl;
		else 
			cout << "Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
	}
	
	return 0;
}
